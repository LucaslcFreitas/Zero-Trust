import socket
import ssl
import concurrent.futures
import json
import os
from policy_enforcement_point import PolicyEnforcementPoint

config = None
config_file = os.path.dirname(os.path.abspath(__file__)) + "/config.json"
try:
    with open(config_file) as file:
        config = json.load(file)
except:
    exit()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((config['ip_address'], config['port']))
    sock.listen()

    print('Servidor Zero Trust iniciado')
    # print(f'Aguardando por conexões em {config['ip_address']}:{config.port}')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            conn, addr = sock.accept()
            print(f'Conexão recebida')

            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain('server.crt', 'server.key')
            conn = context.wrap_socket(conn, server_side=True)

            pep = PolicyEnforcementPoint(conn, addr)

            executor.submit(pep.request)