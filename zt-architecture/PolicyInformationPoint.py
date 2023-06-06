import psycopg2
import os
import json
import datetime

class PolicyInformationPoint:

    def __init__(self) -> None:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json") as file:
            self.config = json.load(file)
        self.connection = None
        self.connect()

    def connect(self) -> None:
        self.connection = psycopg2.connect(
            host=self.config["dbHost"],
            port=self.config["dbPort"],
            database=self.config["dbDatabase"],
            user=self.config["dbUser"],
            password=self.config["dbPassword"]
        )

    def closeConnection(self) -> None:
        if self.connection:
            self.connection.close()

    def getUserAttributes(self, token) -> json:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT nome, tipo, cpf FROM \"zt-ehealth\".\"Usuario\" WHERE id = (SELECT \"idUsuario\" FROM \"zt-ehealth\".\"Token\" WHERE hash = '"+token+"')")
                result = cursor.fetchone()
                if result:
                    return {
                        "name": result[0],
                        "type": result[1],
                        "registry": result[2]
                    }
                return None
        except Exception as e:
            print(e)
            return None
        
    def getEmployeeAttributes(self, cpf) -> json:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"Profissional\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"')")
                result = cursor.fetchone()
                if result:
                    return {
                        "type": result[1],
                        "workDays": result[2],
                        "wrokStart": result[4],
                        "workEnd": result[5]
                    }
                return None
        except Exception as e:
            print(e)
            return None

    def checkTokenValidity(self, token, currentDate) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT validade FROM \"zt-ehealth\".\"Token\" WHERE hash = '" + token + "' AND status = 'Ativo'")
                validity = cursor.fetchone()[0]
                if validity:
                    if (datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) <= validity):
                        return True
                    else:
                        cursor.execute("UPDATE \"zt-ehealth\".\"Token\" SET status='Inativo' WHERE hash = '"+token+"'")
                        self.connection.commit()
                return False
        except Exception as e:
            print(e)
            return False
        
    def checkPasswordValidity(self, cpf, pswToken):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"Senha\" WHERE senha = '"+pswToken+"' AND status = 'Ativo' and \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"')")
                result = cursor.fetchone()
                if result:
                    return True
                return False
        except Exception as e:
            print(e)
            return False
        
    def getResourceSensibilityByName(self, resourceName, subResourceName, typeAction) -> float:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT sensibilidade FROM \"zt-ehealth\".\"SensibilidadeSubRecurso\" WHERE \"tipoAcao\" = '"+typeAction+"' AND \"idSubRecurso\" = (SELECT id FROM \"zt-ehealth\".\"SubRecurso\" WHERE nome = '"+subResourceName+"' AND \"idRecurso\" = (SELECT id FROM \"zt-ehealth\".\"Recurso\" WHERE nome = '"+resourceName+"'))")
                result = cursor.fetchone()
                if result:
                    return result[0]
                return None
        except Exception as e:
            print(e)
            return None
    
    def getResourceSocketByName(self, resourceName) -> json:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT \"ipAddress\", porta FROM \"zt-ehealth\".\"Recurso\" WHERE nome = '"+resourceName+"'")
                result = cursor.fetchone()
                if result:
                    return {
                        'ipAddress': result[0],
                        'port': result[1]
                    }
                return None
        except Exception as e:
            print(e)
            return None
    
    def getSubResourceSocketByName(self, resourceName, subResourceName) -> json:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT r.\"ipAddress\", r.porta FROM \"zt-ehealth\".\"Recurso\" AS r INNER JOIN \"zt-ehealth\".\"SubRecurso\" AS s ON r.id = s.\"idRecurso\" WHERE r.nome = '"+resourceName+"' AND s.nome = '"+subResourceName+"'")
                result = cursor.fetchone()
                if result:
                    return {
                        'ipAddress': result[0],
                        'port': result[1]
                    }
                return None
        except Exception as e:
            print(e)
            return None
    
    def getResourceSocketBySubResourceId(self, subResourceId) -> json:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT \"ipAddress\", porta FROM \"zt-ehealth\".\"Recurso\" WHERE id = (SELECT \"idRecurso\" FROM \"zt-ehealth\".\"SubRecurso\" WHERE id = "+str(subResourceId)+")")
                result = cursor.fetchone()
                if result:
                    return {
                        'ipAddress': result[0],
                        'port': result[1]
                    }
                return None
        except Exception as e:
            print(e)
            return None
        
    def checkResourceUserPermissions(self, tokenUser, resourceName, subResourceName, typeAction, currentDate) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"Permissao\" WHERE \"idUsuario\" = (SELECT \"idUsuario\" FROM \"zt-ehealth\".\"Token\" WHERE hash = '"+tokenUser+"' AND status = 'Ativo' AND validade >= '"+str(currentDate)+"' ) AND \"idSubRecurso\" = (SELECT id FROM \"zt-ehealth\".\"SubRecurso\" WHERE nome = '"+subResourceName+"' AND \"idRecurso\" = (SELECT id FROM \"zt-ehealth\".\"Recurso\" WHERE nome = '"+resourceName+"')) AND \"tipoAcao\" = '"+typeAction+"'")
                result = cursor.fetchone()
                if result:
                    return True
                return False
        except Exception as e:
            print(e)
            return False
        
    def checkLogin(self, cpf, pswToken) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"Senha\" WHERE senha = '"+pswToken+"' AND \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND status = 'Ativo'")
                result = cursor.fetchone()
                if result:
                    return True
                return False
        except Exception as e:
            print(e)
            return False
    
    def registerLoginAndToken(self, cpf, pswToken, date, result, userToken, validity) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO \"zt-ehealth\".\"RegLogin\"(\"idUsuario\", data, resultado, \"idSenha\") VALUES ((SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"'), '"+date+"', '"+result+"', (SELECT id FROM \"zt-ehealth\".\"Senha\" WHERE senha = '"+pswToken+"' AND status = 'Ativo' AND \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"'))) RETURNING id")
                regLoginId = cursor.fetchone()[0]

                if regLoginId and result == 'Permitido':
                    cursor.execute("UPDATE \"zt-ehealth\".\"Token\" SET status='Inativo' WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND status = 'Ativo'")
                    cursor.execute("INSERT INTO \"zt-ehealth\".\"Token\"(\"idUsuario\", \"idRegLogin\", hash, validade, status) VALUES ((SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"'), "+str(regLoginId)+", '"+userToken+"', '"+str(validity)+"', 'Ativo')")
                    self.connection.commit()
                    return True
                self.connection.commit()
                return False
        except Exception as e:
            print(e)
            return False
        
    def updatePassword(self, cpf, token, date) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE \"zt-ehealth\".\"Senha\" SET status='Inativo' WHERE status='Ativo' AND \"idUsuario\"=(SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"')")
                cursor.execute("INSERT INTO \"zt-ehealth\".\"Senha\"(\"idUsuario\", senha, \"dataCriacao\", status) VALUES ((SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"'), '"+token+"', '"+date+"', 'Ativo')")
                rows_affected = cursor.rowcount
                if rows_affected > 0:
                    self.connection.commit()
                    return True
                return False
        except Exception as e:
            print(e)
            return False
    
    def getUserWorkPeriod(self, cpf) -> json:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"' AND tipo = 'Profissional'")
                idUser = cursor.fetchone()[0]
                if idUser:
                    cursor.execute("SELECT * FROM \"zt-ehealth\".\"Profissional\" WHERE \"idUsuario\" = '"+str(idUser)+"'")
                    result = cursor.fetchone()
                    return {
                        "startWorkTime": result[4],
                        "endWorkTime": result[5],
                        "daysWork": result[2]
                    }
                return None
        except Exception as e:
            print(e)
            return None
        
    def getUserPasswordHistory(self, cpf, currentDate) -> list:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=72)
                cursor.execute("SELECT \"dataCriacao\", status FROM \"zt-ehealth\".\"Senha\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND \"dataCriacao\" >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
        
    def getRegLoginHistory(self, cpf, currentDate) -> list:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=72)
                cursor.execute("SELECT data, resultado FROM \"zt-ehealth\".\"RegLogin\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND data >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
        
    def getRecentLocationAccessUser(self, cpf, currentDate) -> list:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=3) #3 horas
                cursor.execute("SELECT latitude, longitude, data, resultado FROM \"zt-ehealth\".\"Acesso\" WHERE resultado = 'Permitido' AND \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND data >= '"+str(date)+"' LIMIT 3")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
        
    def getHistoryLocationAccessUser(self, cpf, currentDate) -> list:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=720) #30 dias
                cursor.execute("SELECT latitude, longitude, data, resultado FROM \"zt-ehealth\".\"Acesso\" WHERE resultado = 'Permitido' AND \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND data >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
    
    def getRecentReducedPrivilege(self, cpf, currentDate):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=336) #2 semanas
                cursor.execute("SELECT status, \"dataExclusao\" FROM \"zt-ehealth\".\"Permissao\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND status = 'Inativo' AND \"dataExclusao\" >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None

    def getRecentNetworkUse(self, cpf, currentDate):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=3) #3 horas
                cursor.execute("SELECT rede, data FROM \"zt-ehealth\".\"Acesso\" WHERE resultado = 'Permitido' AND \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND data >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
    
    def getAcessHistoricByUser(self, cpf, currentDate):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=336) #2 semanas
                cursor.execute("SELECT \"idUsuario\", \"idToken\", \"idPermissao\", \"idSubRecurso\", \"idSensibilidadeSubRecurso\", \"idDispositivo\", latitude, longitude, data, resultado, rede, confianca FROM \"zt-ehealth\".\"Acesso\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND data >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None

    def getAcessHistoricByDevice(self, MAC, currentDate):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=336) #2 semanas
                cursor.execute("SELECT \"idUsuario\", \"idToken\", \"idPermissao\", \"idSubRecurso\", \"idSensibilidadeSubRecurso\", \"idDispositivo\", latitude, longitude, data, resultado, rede, confianca FROM \"zt-ehealth\".\"Acesso\" WHERE \"idDispositivo\" = (SELECT id FROM \"zt-ehealth\".\"Dispositivo\" WHERE \"MAC\" = '"+MAC+"') AND data >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
        
    def getAccessHistoryWithSensibility(self, cpf, currentDate):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=336) #2 semanas
                cursor.execute("SELECT ac.*, se.sensibilidade FROM \"zt-ehealth\".\"Acesso\" AS ac INNER JOIN (SELECT atP.id AS ipt, atS.* FROM \"zt-ehealth\".\"Permissao\" AS atP INNER JOIN \"zt-ehealth\".\"SensibilidadeSubRecurso\" AS atS ON atP.\"idSubRecurso\" = atS.\"idSubRecurso\" AND atp.\"tipoAcao\" = ats.\"tipoAcao\") AS se ON ac.\"idPermissao\" = se.ipt WHERE ac.\"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND ac.data >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None

    def getDeviceByMAC(self, MAC):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"CaracteristicaDispositivo\" AS c INNER JOIN \"zt-ehealth\".\"Dispositivo\" AS d ON c.\"idDispositivo\"= d.id WHERE d.\"MAC\" = '"+MAC+"' AND c.status = 'Ativo'")
                result = cursor.fetchone()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
        
    def getDeviceById(self, id):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"CaracteristicaDispositivo\" AS c INNER JOIN \"zt-ehealth\".\"Dispositivo\" AS d ON c.\"idDispositivo\"= d.id WHERE d.id = '"+str(id)+"' AND c.status = 'Ativo'")
                result = cursor.fetchone()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None

    def checkRecentDeviceChanges(self, MAC, currentDate):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                date = datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=72) #3 dias
                cursor.execute("SELECT \"deviceFingerPrint\", \"sistemaOperacional\", \"versaoSO\", data, status FROM \"zt-ehealth\".\"CaracteristicaDispositivo\" WHERE \"idDispositivo\" = (SELECT id FROM \"zt-ehealth\".\"Dispositivo\" WHERE \"MAC\" = '"+MAC+"') AND data >= '"+str(date)+"'")
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None

    def registerDevice(self, MAC, deviceFingerPrint, SO, versionSO, date) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO \"zt-ehealth\".\"Dispositivo\"(\"MAC\") VALUES ('"+MAC+"') RETURNING id")
                deviceId = cursor.fetchone()[0]

                if deviceId:
                    cursor.execute("INSERT INTO \"zt-ehealth\".\"CaracteristicaDispositivo\"(\"deviceFingerPrint\", \"sistemaOperacional\", \"versaoSO\", data, status, \"idDispositivo\") VALUES ('"+deviceFingerPrint+"', '"+SO+"', '"+versionSO+"', '"+date+"', 'Ativo', "+str(deviceId)+")")
                    self.connection.commit()
                    return True
                return False
        except Exception as e:
            print(e)
            return False
        
    def updateDeviceCharacteristic(self, MAC, deviceFingerPrint, SO, versionSO, date) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("UPDATE \"zt-ehealth\".\"CaracteristicaDispositivo\" SET status='Inativo' WHERE \"idDispositivo\" = (SELECT id FROM \"zt-ehealth\".\"Dispositivo\" WHERE \"MAC\" = '"+MAC+"') AND status = 'Ativo'")
                updated = cursor.rowcount

                if updated > 0:
                    cursor.execute("INSERT INTO \"zt-ehealth\".\"CaracteristicaDispositivo\"(\"deviceFingerPrint\", \"sistemaOperacional\", \"versaoSO\", data, status, \"idDispositivo\") VALUES ('"+deviceFingerPrint+"', '"+SO+"', '"+versionSO+"', '"+date+"', 'Ativo', (SELECT id FROM \"zt-ehealth\".\"Dispositivo\" WHERE \"MAC\" = '"+MAC+"'))")
                    self.connection.commit()
                    return True
                return False
        except Exception as e:
            print(e)
            return False
    
    def getAverageTrustAccess(self, cpf) -> float:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT AVG(confianca) FROM \"zt-ehealth\".\"Acesso\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"')")
                result = cursor.fetchone()
                if result:
                    return result[0]
                return 0
        except Exception as e:
            print(e)
            return 0

    def registerAccess(self, cpf, token, latitude, longitude, MAC, date, ipAddress, result, trust, resourceName, subResourceName, typeAction):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO \"zt-ehealth\".\"Acesso\"(\"idUsuario\", \"idToken\", \"idPermissao\", \"idSubRecurso\", \"idSensibilidadeSubRecurso\", \"idDispositivo\", latitude, longitude, data, resultado, rede, confianca) VALUES ((SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"'), (SELECT id FROM \"zt-ehealth\".\"Token\" WHERE hash = '"+token+"' AND status = 'Ativo'), (SELECT id FROM \"zt-ehealth\".\"Permissao\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') AND \"idSubRecurso\" = ((SELECT id FROM \"zt-ehealth\".\"SubRecurso\" WHERE nome = '"+subResourceName+"' AND \"idRecurso\" = (SELECT id FROM \"zt-ehealth\".\"Recurso\" WHERE nome = '"+resourceName+"'))) AND \"tipoAcao\" = '"+typeAction+"' AND status = 'Ativo'), (SELECT id FROM \"zt-ehealth\".\"SubRecurso\" WHERE nome = '"+subResourceName+"' AND \"idRecurso\" = (SELECT id FROM \"zt-ehealth\".\"Recurso\" WHERE nome = '"+resourceName+"')), (SELECT id FROM \"zt-ehealth\".\"SensibilidadeSubRecurso\" WHERE \"idSubRecurso\" = (SELECT id FROM \"zt-ehealth\".\"SubRecurso\" WHERE nome = '"+subResourceName+"' AND \"idRecurso\" = (SELECT id FROM \"zt-ehealth\".\"Recurso\" WHERE nome = '"+resourceName+"')) AND \"tipoAcao\" = '"+typeAction+"'), (SELECT id FROM \"zt-ehealth\".\"Dispositivo\" WHERE \"MAC\" = '"+MAC+"'), '"+latitude+"', '"+longitude+"', '"+date+"', '"+result+"', '"+ipAddress+"', '"+str(trust)+"') RETURNING id")
                accessId = cursor.fetchone()[0]
                self.connection.commit()
                if accessId:
                    return accessId
                return None
        except Exception as e:
            print(e)
            return None
    
    def registerAccessForReauthenticate(self, idUser, token, idPermission, idSubResource, idSensibility, idDevice, latitude, longitude, date, result, ip, trust):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO \"zt-ehealth\".\"Acesso\"(\"idUsuario\", \"idToken\", \"idPermissao\", \"idSubRecurso\", \"idSensibilidadeSubRecurso\", \"idDispositivo\", latitude, longitude, data, resultado, rede, confianca) VALUES ("+str(idUser)+", (SELECT id FROM \"zt-ehealth\".\"Token\" WHERE hash = '"+token+"' AND status = 'Ativo'), "+str(idPermission)+", "+str(idSubResource)+", "+str(idSensibility)+", "+str(idDevice)+", '"+latitude+"', '"+longitude+"', '"+date+"', '"+result+"', '"+ip+"', "+str(trust)+") RETURNING id")
                accessId = cursor.fetchone()[0]
                self.connection.commit()
                if accessId:
                    return accessId
                return None
        except Exception as e:
            print(e)
            return None
        
    def getAccessById(self, id):
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"Acesso\" WHERE id = "+str(id)+"")
                result = cursor.fetchone()
                self.connection.commit()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None