import socket
import ssl
import os
import json
import time

HOST = '127.0.0.1'
PORT = 5000

def startAccess(test):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Dados dos usuários
        users = {}

        # Arquivo com as instâncias de acesso
        with open(os.path.dirname(os.path.abspath(__file__)) + "/scenarios/"+test+".json") as file:
            instance = json.load(file)
        
        # Conexão com o servidor Zero Trust (aceitando certificado ssl auto assinado)
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        conn = context.wrap_socket(sock, server_hostname=HOST)

        conn.connect((HOST, PORT))
        print(f'Conected to {HOST}:{PORT}')

        average_time = 0.0
        access_count = 0

        if instance:
            for access in instance:
                match (access['TYPE']):
                    case 'LOGIN':
                        message = getLogin(access['REGISTRY'], access['PASSWORD'], access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])

                        conn.sendall(message.encode('utf-8'))

                        data = conn.recv(1024)
                        response = data.decode('utf-8')
                        lines = response.strip().split('\n')
                        data = {}
                        data['RESULT'] = lines[0]
                        for line in lines[1:]:
                            key, value = line.split(' ', 1)
                            data[key] = value
                        if data['RESULT'] == 'AUTHORIZED_LOGIN':
                            if access['REGISTRY'] not in users:
                                users[access['REGISTRY']] = {'PASSWORD': None, 'TOKEN': None}
                            users[access['REGISTRY']]['PASSWORD'] = access['PASSWORD']
                            users[access['REGISTRY']]['TOKEN'] = data['TOKEN']
                            print(data['RESULT'])
                        elif users[access['REGISTRY']]['TOKEN'] == None:
                            print("Login error")
                            break
                    
                    case 'ACCESS':
                        message = getAccess(access['RESOURCE'], access['SUB_RESOURCE'], access['TYPE_ACTION'], users[access['REGISTRY']]['TOKEN'], access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'],  access['VERSION_OS'], access['TIME'])
                                                
                        time_start = time.time()

                        conn.sendall(message.encode('utf-8'))
                        data = conn.recv(1024)
                        
                        time_end = time.time()

                        response = data.decode('utf-8')

                        average_time += (time_end - time_start)
                        access_count += 1

                        if response == "AUTHENTICATION_REQUIRED" and access['REGISTRY'] in users:
                            message = getLogin(access['REGISTRY'], users[access['REGISTRY']]['PASSWORD'], access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                            
                            conn.sendall(message.encode('utf-8'))

                            data = conn.recv(1024)
                            response = data.decode('utf-8')
                            lines = response.strip().split('\n')
                            data = {}
                            data['RESULT'] = lines[0]
                            for line in lines[1:]:
                                key, value = line.split(' ', 1)
                                data[key] = value
                            if data['RESULT'] == 'AUTHORIZED_LOGIN':
                                users[access['REGISTRY']]['TOKEN'] = data['TOKEN']

                                message = getAccess(access['RESOURCE'], access['SUB_RESOURCE'], access['TYPE_ACTION'], users[access['REGISTRY']]['TOKEN'], access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                                
                                conn.sendall(message.encode('utf-8'))
                                data = conn.recv(1024)
                                response = data.decode('utf-8')
                            elif users[access['REGISTRY']]['TOKEN'] == None:
                                print("Authentication for access error")
                                break

                        if response == "REAUTHENTICATION_REQUIRED" and access['REAUTHENTICATE']:
                            message = getReauthenticate(users[access['REGISTRY']]['TOKEN'], access['REGISTRY'], users[access['REGISTRY']]['PASSWORD'], access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                                                        
                            conn.sendall(message.encode('utf-8'))

                            data = conn.recv(1024)
                            response = data.decode('utf-8')
                            lines = response.strip().split('\n')
                            data = {}
                            data['RESULT'] = lines[0]
                            if data['RESULT'] == "REAUTHENTICATION_ALLOWED":
                                for line in lines[1:]:
                                    key, value = line.split(' ', 1)
                                    data[key] = value
                                users[access['REGISTRY']]['TOKEN'] = data['TOKEN']
                                print(response)
                            else:
                                print(data['RESULT'])
                        else:
                            print(response)

                    case 'UPDATE_PASSWORD':
                        message = getUpdatePassword(users[access['REGISTRY']]['TOKEN'], users[access['REGISTRY']]['PASSWORD'], access['NEW_PASSWORD'], access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                        
                        conn.sendall(message.encode('utf-8'))

                        data = conn.recv(1024)
                        response = data.decode('utf-8')
                        lines = response.strip().split('\n')
                        data = {}
                        data['RESULT'] = lines[0]
                        for line in lines[1:]:
                            key, value = line.split(' ', 1)
                            data[key] = value
                        if data['RESULT'] == 'UPDATED_PASSWORD':
                            users[access['REGISTRY']]['PASSWORD'] = access['NEW_PASSWORD']
                            print(data['RESULT'])
                            users[access['REGISTRY']]['TOKEN'] = data['TOKEN']
                        elif data['RESULT'] == 'UNAUTHORIZED_PASSWORD_UPDATE':
                            print("UNAUTHORIZED_PASSWORD_UPDATE")
                        elif users[access['REGISTRY']]['TOKEN'] == None:
                            print("Update password error")
                            break
            print(f'Tempo médio de acesso: {(average_time/access_count)*1000} ms')

        conn.close()
        print("EFETUE A LIMPEZA DO BANCO DE DADOS ANTES DE REALIZAR O PRÓXIMO CENÁRIO")

    print('Closed connection')

def getLogin(registry, password, ip, latitude, longitude, mac, dfp, os, versionOs, time):
    message = "LOGIN\n"
    message += "REGISTRY " + registry + "\n"
    message += "PASSWORD " + password + "\n"
    message += "IP_ADDRESS " + ip + "\n"
    message += "LATITUDE " + latitude + "\n"
    message += "LONGITUDE " + longitude + "\n"
    message += "MAC " + mac + "\n"
    message += "DFP " + dfp + "\n"
    message += "OS " + os + "\n"
    message += "VERSION_OS " + versionOs + "\n"
    message += "TIME " + time + "\n"
    return message

def getAccess(resource, subResource, typeAction, token, ip, latitude, longitude, mac, dfp, os, versionOs, time):
    message = "ACCESS\n"
    message += "RESOURCE " + resource + "\n"
    message += "SUB_RESOURCE " + subResource + "\n"
    message += "TYPE_ACTION " + typeAction + "\n"
    message += "TOKEN " + token + "\n"
    message += "IP_ADDRESS " + ip + "\n"
    message += "LATITUDE " + latitude + "\n"
    message += "LONGITUDE " + longitude + "\n"
    message += "MAC " + mac + "\n"
    message += "DFP " + dfp + "\n"
    message += "OS " + os + "\n"
    message += "VERSION_OS " + versionOs + "\n"
    message += "TIME " + time + "\n"
    return message

def getReauthenticate(token, registry, password, ip, latitude, longitude, mac, dfp, os, versionOs, time):
    message = "REAUTHENTICATION\n"
    message += "TOKEN " + token + "\n"
    message += "REGISTRY " + registry + "\n"
    message += "PASSWORD " + password + "\n"
    message += "IP_ADDRESS " + ip + "\n"
    message += "LATITUDE " + latitude + "\n"
    message += "LONGITUDE " + longitude + "\n"
    message += "MAC " + mac + "\n"
    message += "DFP " + dfp + "\n"
    message += "OS " + os + "\n"
    message += "VERSION_OS " + versionOs + "\n"
    message += "TIME " + time + "\n"
    return message

def getUpdatePassword(token, oldPassword, newPassword, ip, latitude, longitude, mac, dfp, os, versionOs, time):
    message = "UPDATE_PASSWORD\n"
    message += "TOKEN " + token + "\n"
    message += "OLD_PASSWORD " + oldPassword + "\n"
    message += "NEW_PASSWORD " + newPassword + "\n"
    message += "IP_ADDRESS " + ip + "\n"
    message += "LATITUDE " + latitude + "\n"
    message += "LONGITUDE " + longitude + "\n"
    message += "MAC " + mac + "\n"
    message += "DFP " + dfp + "\n"
    message += "OS " + os + "\n"
    message += "VERSION_OS " + versionOs + "\n"
    message += "TIME " + time + "\n"
    return message

if __name__ == '__main__':
    print("SELECIONE O CENÁRIO:")
    print("1 - Cenário 1 - Acesso Normal")
    print("2 - Cenário 2 - Roubo de Token - Teste 1")
    print("3 - Cenário 2 - Roubo de Token - Teste 2")
    print("4 - Cenário 3 - Roubo de Credenciais")
    print("5 - Cenário 4 - Ataque de Força Bruta - Sem Sucesso")
    print("6 - Cenário 4 - Ataque de Força Bruta - Com Sucesso")
    print("7 - Cenário 5 - Dispositivo Compartilhado")
    print("8 - Cenário 6 - Acesso fora do Horário - Teste 1")
    print("9 - Cenário 6 - Acesso fora do Horário - Teste 2")
    print("10 - Cenário 6 - Acesso fora do Horário - Teste 3")
    print("11 - Cenário 6 - Acesso fora do Horário - Teste 4")
    print("12 - SAIR")

    option = input("Opção: ")
    while option != 13:
        match option:
            case "1":
                startAccess("instance-C1")
            case "2":
                startAccess("instance-C2T1")
            case "3":
                startAccess("instance-C2T2")
            case "4":
                startAccess("instance-C3")
            case "5":
                startAccess("instance-C4T1")
            case "6":
                startAccess("instance-C4T2")
            case "7":
                startAccess("instance-C5")
            case "8":
                startAccess("instance-C6T1")
            case "9":
                startAccess("instance-C6T2")
            case "10":
                startAccess("instance-C6T3")
            case "11":
                startAccess("instance-C6T4")
            case "12":
                break
            case _:
                print("Opção Inválida!")
        option = input("Opção: ")