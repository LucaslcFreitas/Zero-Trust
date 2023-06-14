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
        with open(os.path.dirname(os.path.abspath(__file__)) + "/instance-normal.json") as file:
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
                            registry = access['REGISTRY']
                            password = access['PASSWORD']
                            print(data['RESULT'])
                            token = data['TOKEN']
                        elif token == None:
                            print("Login error")
                            break
                    
                    case 'ACCESS':
                        message = getAccess(access['RESOURCE'], access['SUB_RESOURCE'], access['TYPE_ACTION'], token, access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'],  access['VERSION_OS'], access['TIME'])
                                                
                        conn.sendall(message.encode('utf-8'))

                        data = conn.recv(1024)
                        response = data.decode('utf-8')

                        if response == "AUTHENTICATION_REQUIRED" and registry and password:
                            message = getLogin(registry, password, access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                            
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
                                token = data['TOKEN']

                                message = getAccess(access['RESOURCE'], access['SUB_RESOURCE'], access['TYPE_ACTION'], token, access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                                
                                conn.sendall(message.encode('utf-8'))
                                data = conn.recv(1024)
                                response = data.decode('utf-8')
                            elif token == None:
                                print("Authentication for access error")
                                break

                        if response == "REAUTHENTICATION_REQUIRED" and access['REAUTHENTICATE']:
                            message = getReauthenticate(token, registry, password, access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                                                        
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
                                token = data['TOKEN']
                                print(response)
                            else:
                                print(data['RESULT'])
                        else:
                            print(response)

                    case 'UPDATE_PASSWORD':
                        message = getUpdatePassword(token, password, access['NEW_PASSWORD'], access['IP_ADDRESS'], access['LATITUDE'], access['LONGITUDE'], access['MAC'], access['DFP'], access['OS'], access['VERSION_OS'], access['TIME'])
                        
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
                            password = access['NEW_PASSWORD']
                            print(data['RESULT'])
                            token = data['TOKEN']
                        elif data['RESULT'] == 'UNAUTHORIZED_PASSWORD_UPDATE':
                            print("UNAUTHORIZED_PASSWORD_UPDATE")
                        elif token == None:
                            print("Update password error")
                            break

        conn.close()

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
    connect()