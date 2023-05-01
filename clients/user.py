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
        print(f'Conectado a {HOST}:{PORT}')

        while True:
            message = input('Digite a mensagem para enviar (ou "sair" para encerrar): ')
            if message.lower() == 'sair':
                break

            conn.sendall(message.encode())
            data = conn.recv(1024)
            resposta = data.decode()
            print(f'Recebido do servidor: {resposta}')

    print('Conexão fechada')

if __name__ == '__main__':
    connect()