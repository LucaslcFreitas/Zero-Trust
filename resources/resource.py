import os
import json
import socket
import threading

def start():
    try:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json") as file:
            resources = json.load(file)
    except:
        exit()

    for resource in resources:
        thread = threading.Thread(target=start_resource, args=(resource["resource"], resource["ip_address"], resource["port"]))
        thread.start()

def start_resource(name, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        print(f'Connection received from {addr}')

        # Inicia uma nova thread para tratar a conexão
        t = threading.Thread(target=handle_conection, args=(conn, name))
        t.start()

def handle_conection(conn, resourceName):
    response = resourceName
    conn.sendall(response.encode())
    conn.close()


if __name__ == '__main__':
    start()