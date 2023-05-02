import socket
import ssl

HOST = '127.0.0.1'
PORT = 5000

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Inicia o protocolo TLS
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        conn = context.wrap_socket(sock, server_hostname=HOST)

        conn.connect((HOST, PORT))
        print(f'Conected to {HOST}:{PORT}')

        message = "CONECT electronic_health_record\n"
        message += "USER_TOKEN: 8C3AED472FCB8ACCEB65725835189A89264A9A25E9226355877C75BE0C74D8A0\n"
        message += "IP_ADDRESS: 10.0.0.0\n"
        message += "LOCATION: 21.7755342 -43.3719626\n"
        message += "DEVICE_MAC: 2B-40-C1-4E-34-E2"

        conn.sendall(message.encode())

        data = conn.recv(1024)
        resposta = data.decode()
        print(f'Recebido do servidor: {resposta}')

        conn.close()

    print('Closed connection')

if __name__ == '__main__':
    connect()