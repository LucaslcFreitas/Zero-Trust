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

    def checkTokenValidity(self, token, currentDate) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT validade FROM \"zt-ehealth\".\"Token\" WHERE hash = '" + token + "' AND status = 'Ativo'")
                validity = cursor.fetchone()[0]
                if validity:
                    if (datetime.datetime.strptime(currentDate, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - validity) <= datetime.timedelta(hours=3):
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
        
    def checkResourceUserPermissions(self, tokenUser, resourceName, subResourceName, typeAction) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"Permissao\" WHERE \"idUsuario\" = (SELECT \"idUsuario\" FROM \"zt-ehealth\".\"Token\" WHERE hash = '"+tokenUser+"' AND status = 'Ativo' AND validade < (CURRENT_TIMESTAMP - INTERVAL '1 hour')) AND \"idSubRecurso\" = (SELECT id FROM \"zt-ehealth\".\"SubRecurso\" WHERE nome = '"+subResourceName+"' AND \"idRecurso\" = (SELECT id FROM \"zt-ehealth\".\"Recurso\" WHERE nome = '"+resourceName+"')) AND \"tipoAcao\" = '"+typeAction+"'")
                result = cursor.fetchone()
                if result:
                    return True
                return False
        except Exception as e:
            print(e)
            return False
        
    def checkLogin(self, cpf, token) -> bool:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM \"zt-ehealth\".\"Senha\" WHERE senha = '"+token+"' AND \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"')")
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
                    cursor.execute("INSERT INTO \"zt-ehealth\".\"Token\"(\"idUsuario\", \"idRegLogin\", hash, validade, status) VALUES ((SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"'), "+str(regLoginId)+", '"+userToken+"', '"+validity+"', 'Ativo')")
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
                cursor.execute("UPDATE \"zt-ehealth\".\"Senha\" SET status='Inativo' WHERE status='Ativo' AND id=(SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"')")
                cursor.execute("INSERT INTO \"zt-ehealth\".\"Senha\"(\"idUsuario\", senha, \"dataCriacao\", status) VALUES ((SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"'), '"+token+"', '"+date+"', 'Ativo')")
                rows_affected = cursor.rowcount
                self.connection.commit()
                if rows_affected > 0:
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
                        "horarioTrabalhoInicio": result[4],
                        "horarioTrabalhoFinal": result[5],
                        "diasTrabalho": result[2]
                    }
                return None
        except Exception as e:
            print(e)
            return None
        
    def getUserPasswordHistory(self, cpf, limit) -> list:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT \"dataCriacao\", status FROM \"zt-ehealth\".\"Senha\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') LIMIT "+str(limit))
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
        
    def getRegLoginHistory(self, cpf, limit) -> list:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT data, resultado FROM \"zt-ehealth\".\"RegLogin\" WHERE \"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+cpf+"') LIMIT "+str(limit))
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
        
    def getLocationAccessUser(self, cpf, limit) -> list:
        if not self.connection:
            self.connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute()
                result = cursor.fetchall()
                if result:
                    return result
                return None
        except Exception as e:
            print(e)
            return None
    
    def privilegioReduzidoRecente():
        print()

    def redeNormalmenteUtilizada():
        print()

    def historicoUsoDispositivo():
        print()

    def getDispositivoPorMAC():
        print()

    def getAcessoHistorico():
        print()

    def registrarDispositivo():
        print()

    def registrarAcesso():
        print()