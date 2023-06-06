import socket
import ssl
import concurrent.futures
import os
import logging
import json
import Response
from PolicyDecisionPoint import PolicyDecisionPoint

class PolicyEnforcementPoint:
    
    def __init__(self) -> None:
        try:
            with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json") as file:
                self.config = json.load(file)
        except:
            exit()
    
    # Inicia o PEP e dispara uma thread para cada requisição
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.config['ip_address'], self.config['port']))
            sock.listen()

            logging.info("Zero Trust server started!")
            logging.info(f'Waiting for connections at {self.config["ip_address"]}:{self.config["port"]}')

            with concurrent.futures.ThreadPoolExecutor() as executor:
                while True:
                    conn, addr = sock.accept()
                    logging.info(f'Connection received from {addr}')

                    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
                    context.load_cert_chain('server.crt', 'server.key')
                    conn = context.wrap_socket(conn, server_side=True)

                    executor.submit(self.handle_client, conn, addr)

    # Thread para tratar requisição do usuário
    def handle_client(self, conn, addr) -> None:
        logging.info(f'Start thred from {addr}')

        pdp = PolicyDecisionPoint()

        opReauthentication = {
            "inReauthentication": False,
            "idAccess": None
        }

        while(True):
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()

            # Operação de reautenticação
            if opReauthentication["inReauthentication"]:
                message += "ID_ACCESS "+str(opReauthentication["idAccess"])+"\n"
        
            try:
                decision, body = pdp.policyAdministrator(message)
            except Exception as e:
                logging.error(e)

            match(decision):
                case Response.ACCESS_ALLOWED: # Conexão autorizada
                    if body["ipAddress"] and body["port"]:
                        logging.info(f'Authorized request for {addr}')
                        sockResource = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sockResource.connect((body["ipAddress"], body["port"]))
                        responseResource = sockResource.recv(1024)
                        conn.sendall(responseResource)
                        sockResource.close()
                    else:
                        logging.error(f'Internal server error')
                        result = "Internal server error"
                        conn.sendall(result.encode())
                case Response.ACCESS_DENIED:
                    logging.info(f'Denied request for {addr}')
                    result = "Denied requisition"
                    conn.sendall(result.encode())
                case Response.RESOURCE_NOT_FOUND:
                    logging.info(f'Denied request for {addr}')
                    result = "Resource not found"
                    conn.sendall(result.encode())
                case Response.AUTHENTICATION_REQUIRED:
                    logging.info(f'Authentication required for {addr}')
                    result = "Authentication required"
                    conn.sendall(result.encode())
                case Response.REAUTHENTICATION_REQUIRED:
                    if body["idAccess"]:
                        logging.info(f'Reauthentication required for {addr}')   
                        opReauthentication["inReauthentication"] = True
                        opReauthentication["idAccess"] = body["idAccess"]
                        result = "Reauthentication required"
                        conn.sendall(result.encode())
                    else:
                        logging.error(f'Internal server error')
                        result = "Internal server error"
                        conn.sendall(result.encode())
                case Response.AUTHORIZED_LOGIN:
                    if body["token"]:
                        logging.info(f'Authorized login for {addr}')
                        conn.sendall(body["token"].encode())
                    else :
                        logging.error(f'Login error for {addr}')
                        result = "Internal server error"
                        conn.sendall(result.encode())
                case Response.INTERNAL_SERVER_ERROR:
                    logging.error(f'Internal server error')
                    result = "Internal server error"
                    conn.sendall(result.encode())
                case _: #default
                    result = "Denied requisition"
                    conn.sendall(result.encode())
                    logging.error(f'Unidentified answer for {addr}')
                    logging.info(f'Connection closed with {addr}')
                    conn.close()
                    break  

            if decision != Response.REAUTHENTICATION_REQUIRED:
                opReauthentication["inReauthentication"] = False
                opReauthentication["idAccess"] = None
        logging.info(f'Connection closed with {addr}')
        conn.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    pep = PolicyEnforcementPoint()
    pep.start()