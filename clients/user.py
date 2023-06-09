import socket
import ssl
import os
import json

HOST = '127.0.0.1'
PORT = 5000

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Dados de usuário
        token = None
        registry = None
        password = None

        # Arquivo com as instâncias de acesso
        with open(os.path.dirname(os.path.abspath(__file__)) + "/userInstance4.json") as file:
            instance = json.load(file)
        
        # Conexão com o servidor Zero Trust (aceitando certificado ssl auto assinado)
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        conn = context.wrap_socket(sock, server_hostname=HOST)

        conn.connect((HOST, PORT))
        print(f'Conected to {HOST}:{PORT}')

        if instance:
            for access in instance:
                match (access['TYPE']):
                    case 'LOGIN':
                        registry = access['REGISTRY']
                        password = access['PASSWORD']

                        message = access['TYPE'] + "\n"
                        message += "REGISTRY " + access['REGISTRY'] + "\n"
                        message += "PASSWORD " + access['PASSWORD'] + "\n"
                        message += "IP_ADDRESS " + access['IP_ADDRESS'] + "\n"
                        message += "LATITUDE " + access['LATITUDE'] + "\n"
                        message += "LONGITUDE " + access['LONGITUDE'] + "\n"
                        message += "MAC " + access['MAC'] + "\n"
                        message += "DFP " + access['DFP'] + "\n"
                        message += "OS " + access['OS'] + "\n"
                        message += "VERSION_OS " + access['VERSION_OS'] + "\n"
                        message += "TIME " + access['TIME'] + "\n"

                        conn.sendall(message.encode('utf-8'))

                        data = conn.recv(1024)
                        resposta = data.decode('utf-8')
                        lines = resposta.strip().split('\n')
                        data = {}
                        data['RESULT'] = lines[0]
                        for line in lines[1:]:
                            key, value = line.split(' ', 1)
                            data[key] = value
                        if data['RESULT'] == 'AUTHORIZED_LOGIN':
                            print(data['RESULT'])
                            token = data['TOKEN']
                        else:
                            print("Login error")
                            break
                    
                    case 'ACCESS':
                        message = "ACCESS\n"
                        message += "RESOURCE " + access['RESOURCE'] + "\n"
                        message += "SUB_RESOURCE " + access['SUB_RESOURCE'] + "\n"
                        message += "TYPE_ACTION " + access['TYPE_ACTION'] + "\n"
                        message += "TOKEN " + token + "\n"
                        message += "IP_ADDRESS " + access['IP_ADDRESS'] + "\n"
                        message += "LATITUDE " + access['LATITUDE'] + "\n"
                        message += "LONGITUDE " + access['LONGITUDE'] + "\n"
                        message += "MAC " + access['MAC'] + "\n"
                        message += "DFP " + access['DFP'] + "\n"
                        message += "OS " + access['OS'] + "\n"
                        message += "VERSION_OS " + access['VERSION_OS'] + "\n"
                        message += "TIME " + access['TIME'] + "\n"
                        
                        conn.sendall(message.encode('utf-8'))

                        data = conn.recv(1024)
                        resposta = data.decode('utf-8')

                        if resposta == "REAUTHENTICATION_REQUIRED":
                            message = "REAUTHENTICATION\n"
                            message += "TOKEN " + token + "\n"
                            message += "REGISTRY " + registry + "\n"
                            message += "PASSWORD " + password + "\n"
                            message += "IP_ADDRESS " + access['IP_ADDRESS'] + "\n"
                            message += "LATITUDE " + access['LATITUDE'] + "\n"
                            message += "LONGITUDE " + access['LONGITUDE'] + "\n"
                            message += "MAC " + access['MAC'] + "\n"
                            message += "DFP " + access['DFP'] + "\n"
                            message += "OS " + access['OS'] + "\n"
                            message += "VERSION_OS " + access['VERSION_OS'] + "\n"
                            message += "TIME " + access['TIME'] + "\n"
                            
                            conn.sendall(message.encode('utf-8'))

                            data = conn.recv(1024)
                            resposta = data.decode('utf-8')
                            lines = resposta.strip().split('\n')
                            data = {}
                            data['RESULT'] = lines[0]
                            if data['RESULT'] == "REAUTHENTICATION_ALLOWED":
                                for line in lines[1:]:
                                    key, value = line.split(' ', 1)
                                    data[key] = value
                                token = data['TOKEN']
                                print(resposta)
                            else:
                                print(data['RESULT'])
                        else:
                            print(resposta)
        conn.close()

    print('Closed connection')

if __name__ == '__main__':
    connect()