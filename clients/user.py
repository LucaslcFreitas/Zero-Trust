import socket
import ssl
import datetime
import hashlib
import platform

HOST = '127.0.0.1'
PORT = 5000

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        conn = context.wrap_socket(sock, server_hostname=HOST)

        conn.connect((HOST, PORT))
        print(f'Conected to {HOST}:{PORT}')

        # message = "LOGIN\n"
        # message += "REGISTRY 460.395.930-32\n"
        # message += "PASSWORD URtrE4lfJ7\n"
        # message += "IP_ADDRESS 172.16.10.1\n"
        # message += "LATITUDE 21.7755342\n"
        # message += "LONGITUDE -43.3719626\n"
        # message += "MAC CA-14-17-8F-9E-9G\n"
        # message += "DFP 29930a0e2ea9e88d47e59571862aaf2c01781cbef7dbac0615e9efe383c8235b\n"
        # message += "OS Windows-10-10.0.19045-SP0\n"
        # message += "VERSION_OS 20H2\n"
        # message += "TIME 2023-05-29 10:45:58.649878\n"

        message = "ACCESS\n"
        message += "RESOURCE Registro Eletrônico de Saúde\n"
        message += "SUB_RESOURCE Notas Clínicas\n"
        message += "TYPE_ACTION Escrita\n"
        message += "TOKEN 5c934c33e0a203e2a6865a530daaa036836aad06e38bffc5a49aadb80c0d6227\n"
        message += "IP_ADDRESS 172.16.10.1/24\n"
        message += "LATITUDE -21.7755342\n"
        message += "LONGITUDE -43.3719626\n"
        message += "MAC CA-14-17-8F-9E-9F\n"
        message += "DFP 29930a0e2ea9e88d47e59571862aaf2c01781cbef7dbac0615e9efe383c8235b\n"
        message += "OS Windows 10\n"
        message += "VERSION_OS 21H2\n"
        message += "TIME 2023-06-04 23:36:19.047062\n"

        # message = "UPDATE_PASSWORD\n"
        # message += "TOKEN a73598d1e41235360363faff1d7876462429b2461d5cbedd01c19cd5b58275c2\n"
        # message += "OLD_PASSWORD URtrE4lfJ7\n"
        # message += "NEW_PASSWORD exuXJ1Cthq\n"
        # message += "IP_ADDRESS 172.16.10.1/24\n"
        # message += "LATITUDE -21.7755342\n"
        # message += "LONGITUDE -43.3719626\n"
        # message += "MAC CA-14-17-8F-9E-9F\n"
        # message += "DFP 29930a0e2ea9e88d47e59571862aaf2c01781cbef7dbac0615e9efe383c8235b\n"
        # message += "OS Windows-10-10.0.19045-SP0\n"
        # message += "VERSION_OS 20H2\n"
        # message += "TIME 2023-06-04 23:24:19.047062\n"

        conn.sendall(message.encode())

        data = conn.recv(1024)
        resposta = data.decode()

        print(f'Recebido do servidor: {resposta}')
        if resposta == 'Reauthentication required':
            message = "REAUTHENTICATION\n"
            message += "TOKEN 5c934c33e0a203e2a6865a530daaa036836aad06e38bffc5a49aadb80c0d6227\n"
            message += "REGISTRY 460.395.930-32\n"
            message += "PASSWORD URtrE4lfJ7\n"
            message += "IP_ADDRESS 172.16.10.1/24\n"
            message += "LATITUDE -21.7755342\n"
            message += "LONGITUDE -43.3719626\n"
            message += "MAC CA-14-17-8F-9E-9F\n"
            message += "DFP 29930a0e2ea9e88d47e59571862aaf2c01781cbef7dbac0615e9efe383c8235b\n"
            message += "OS Windows 10\n"
            message += "VERSION_OS 21H2\n"
            message += "TIME 2023-06-04 23:37:19.047062\n"

            conn.sendall(message.encode())
            data = conn.recv(1024)
            resposta = data.decode()

            print(f'Recebido do servidor: {resposta}')
        else:
            print("n deu n")

        conn.close()

    print('Closed connection')

if __name__ == '__main__':
    connect()
    # print(platform.platform())
    # print(datetime.datetime.now() + datetime.timedelta(hours=3))
    #print(datetime.time(9,58, 36))
    # print(datetime.datetime.now())
    # senha = f'6CQ3jhgO1I{datetime.datetime.now()}'
    # senha = f'URtrE4lfJ7'
    # print(hashlib.sha256(senha.encode('utf-8')).hexdigest())

    # # Obtém a data e hora atual
    # agora = datetime.datetime.now()

    # # Define a duração de uma hora usando timedelta
    # uma_hora = datetime.timedelta(hours=1)

    # # Adiciona uma hora à data e hora atual
    # nova_data_hora = agora + uma_hora

    # # Imprime a nova data e hora
    # print(agora)
    # print(nova_data_hora)
    # data = datetime.datetime(2023, 5, 27)
    # nome_dia_da_semana = datetime.date(data.year, data.month, data.day).strftime('%A')
    # print(nome_dia_da_semana)