


class PolicyEnforcementPoint:
    
    
    def __init__(self, conn, addr) -> None:
        self.conn = conn
        self.addr = addr
    
    def request(self) -> None:
        print(f'Conexão estabelecida por {self.addr}')

        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f'Mensagem recebida de {self.addr}: {message}')

            # Aqui você pode adicionar o código para processar a mensagem

            resposta = f'Você disse: {message}'
            self.conn.sendall(resposta.encode())

        print(f'Conexão fechada com {self.addr}')
        self.conn.close()