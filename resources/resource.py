import os
import json
import socket
import threading

def start():
    try:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json") as file:
            config = json.load(file)
    except:
        exit()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((config['ip_address'], config['port']))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        print(f'Connection received from {addr}')

        # Inicia uma nova thread para tratar a conexão
        t = threading.Thread(target=handle_conection, args=(conn, addr))
        t.start()

def handle_conection(conn, addr):
    response = "resource answer"
    conn.sendall(response.encode())
    conn.close()


if __name__ == '__main__':
    start()