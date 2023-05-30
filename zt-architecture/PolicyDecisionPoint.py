import logging
import json
import datetime
import random
import hashlib
import math
from geopy.distance import geodesic
import Response
import TypeRequest
from PolicyInformationPoint import PolicyInformationPoint

class PolicyDecisionPoint:

    def __init__(self) -> None:
        self.pip = PolicyInformationPoint()

    def policyAdministrator(self, message):
        lines = message.strip().split('\n')
        data = {}

        data['TYPE'] = lines[0]
        for line in lines[1:]:
            key, value = line.split(' ', 1)
            data[key] = value

        match(data['TYPE']):
            case TypeRequest.LOGIN:
                if (data['REGISTRY'] and data['PASSWORD'] and data['IP_ADDRESS'] and data['LATITUDE'] and data['LONGITUDE'] and data['MAC'] and data['DFP'] and data['OS'] and data['VERSION_OS'] and data['TIME']):
                    result = self.__login(data['REGISTRY'], data['PASSWORD'], data['TIME'])
                    #self.__checkAndRegisterDevice(data['MAC'], data['DFP'], data['OS'], data['VERSION_OS'], data['TIME'])
                    if result:
                        return result
                    else:
                        return Response.ACCESS_DENIED
                return Response.ACCESS_DENIED
            case TypeRequest.ACCESS:
                if (data['RESOURCE'] and data['SUB_RESOURCE'] and data['TYPE_ACTION'] and data['TOKEN'] and data['IP_ADDRESS'] and data['LATITUDE'] and data['LONGITUDE'] and data['MAC'] and data['DFP'] and data['OS'] and data['VERSION_OS'] and data['TIME']):
                    return self.policyEngine(data)
            case _: # Default
                return Response.ACCESS_DENIED

    def policyEngine(self, data):
        # Verifica se o usuário está devidamente autenticado
        if not self.__checkUserCredentials(data['TOKEN'], data['TIME']):
            #registrar acesso negado...
            return Response.AUTHENTICATION_REQUIRED

        # Verifica se o recurso e subrecurso existe
        if not self.pip.getSubResourceSocketByName(data['RESOURCE'], data['SUB_RESOURCE']):
            return Response.RESOURCE_NOT_FOUND

        # Verifica se o usuário possui permissão para acessar o recurso
        if not self.pip.checkResourceUserPermissions(data['TOKEN'], data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'], data['TIME']):
            return Response.ACCESS_DENIED

        # Pega as credênciais do usuário
        user = self.pip.getUserAttributes(data['TOKEN'])

        # Calcula a confiança com base no usuário e contexto
        try:
            userTrust = self.__evaluateUserAtributesAndContext(user['registry'], data['TIME'], data['LATITUDE'], data['LONGITUDE'])
        except Exception as e:
            print(e)
        # Calcula a confiança com base no dispositivo do usuário
        deviceTrust = self.__evaluateUserDevice(data['MAC'], data['DFP'], data['OS'], data['VERSION_OS'], data['TIME'])

        # Calcula a confiança com base no histórico de acesso
        # historyTrust = self.__evaluateUserHistory()

        # Pega a sensibilidade do recurso
        # sensitivity = self.__evaluateResourceSensibility()

        #Calcula a confinça final
        # trust = 0
        # if historyTrust == 0:
        #     trust = math.sqrt(userTrust * deviceTrust) * 0.01
        # else:
        #     trust = math.sqrt(userTrust * deviceTrust) * (historyTrust/100)
        
        return Response.ACCESS_ALLOWED

    # Realiza login do usuário
    def __login(self, registry, password, date) -> str:
        pswToken = hashlib.sha256(str(password).encode()).hexdigest()
        auxUserToken = registry + password + str(datetime.datetime.now()) + str(random.randint(1, 100000))
        userToken = hashlib.sha256(str(auxUserToken).encode()).hexdigest()
        validity = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(hours=3)
        result = 'Negado'

        if self.pip.checkLogin(registry, pswToken):
            result = 'Permitido'

        self.pip.registerLoginAndToken(registry, pswToken, date, result, userToken, validity)
        if result == 'Permitido':
            return userToken
        return None
    
    # Verifica um novo dispositivo e o registra
    def __checkAndRegisterDevice(self, MAC, DFP, OS, versionOS, date):
        if not self.pip.getDeviceByMAC(MAC):
            self.pip.registerDevice(MAC, DFP, OS, versionOS, date)

    # Realiza reautenticação do usuário
    def __reauthenticate(self):
        logging.info("Reauthenticate")

    # Valida se o usuário está devidamente autenticado
    def __checkUserCredentials(self, token, date):
        if not len(token) == 64:
            return False
        
        return self.pip.checkTokenValidity(token, date)
    
    # Avalia os atributos do usuário
    def __evaluateUserAtributesAndContext(self, registry, date, latitude, longitude) -> float:
        trust = 100.0
        
        # Avalia logins recentes
        recentLogins = self.pip.getRegLoginHistory(registry, date)
        countFailedLogins = 0
        if recentLogins:
            for login in recentLogins:
                if login[1] == 'Negado':
                    countFailedLogins += 1
        if countFailedLogins >= 1 and countFailedLogins < 4:
            trust -= 5
        elif countFailedLogins >= 4 and countFailedLogins < 7:
            trust -= 9
        elif countFailedLogins >= 7:
            trust -= 13
        

        # Avalia troca de senhas recentes
        recentPasswordChanges = self.pip.getUserPasswordHistory(registry, date)
        countPasswordChanges = 0
        if recentPasswordChanges:
            countPasswordChanges = len(recentPasswordChanges)
        if countPasswordChanges > 1 and countPasswordChanges < 3:
            trust -= 5
        elif countPasswordChanges >= 3 and countPasswordChanges < 6:
            trust -= 15
        elif countPasswordChanges >= 6:
            trust -= 20
        
        # Avalia mudanca consideravel na localizacao recente
        recentLocations = self.pip.getRecentLocationAccessUser(registry, date) # Avaliação com base nos acessos recentes, para detectar mudanças bruscas na localização
        baseLocations = self.pip.getHistoryLocationAccessUser(registry) # Avaliação de toda base de acesso, para detectar acesso fora da região de costume
        if recentLocations:
            for recenteLoc in recentLocations:
                timeR = ((datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - recenteLoc[2]).total_seconds() / 3600) / 24 # Diferença do tempo atual em relação ao acesso, normalizado (0, 1)
                distanceR = geodesic((latitude, longitude), (recenteLoc[0], recenteLoc[1])).meters
                diferenceR = distanceR / (timeR * 50000)
                if (diferenceR > 1 and diferenceR < 1.3):
                    trust -= 10
                elif (diferenceR >= 1.3 and diferenceR < 1.5):
                    trust -= 20
                elif (diferenceR >= 1.5 and diferenceR < 2.0):
                    trust -= 35
                elif diferenceR >= 2.0:
                    trust -= 50
        if baseLocations:
            zones = []
            for baseLoc in baseLocations:
                allocated = False
                for zone in zones:
                    distZone = geodesic((zone['latitude'], zone['longitude']), (baseLoc[0], baseLoc[1])).meters
                    if distZone < 1000:
                        zone['count'] += 1
                        allocated = True
                        break
                if not allocated:
                    zones.append({
                        'latitude': baseLoc[0],
                        'longitude': baseLoc[1],
                        'count': 1
                    })
            auxZone = None
            for zone in zones:
                dist = geodesic((zone['latitude'], zone['longitude']), (latitude, longitude)).meters
                if dist < 1000:
                    auxZone = zone
                    break
            if auxZone:
                if auxZone['count'] < 5:
                   trust -= 40
                elif auxZone['count'] < 10:
                    trust -= 30
                elif auxZone['count'] < 15:
                    trust -= 15
            else:
                trust -= 40
        else:
            trust -= 40
        

        # Avalia horário de acesso
        # workPeriod = self.pip.getUserWorkPeriod(registry)
        # if workPeriod:
        #     days = workPeriod['daysWork'].split("-")

        # Avalia reduções de privilégios recentes
        reducedPrivileges = self.pip.getRecentReducedPrivilege(registry, date)
        for privilege in reducedPrivileges:
            if privilege[0] == 'Inativo':
                trust -= 10

        # Avalia mudança de rede de acesso

        if trust > 0:
            return trust
        return 0

    # Avalia o dispositivo utilizado pelo usuário
    def __evaluateUserDevice(self, MAC, dfp, os, versionOs, date) -> float:
        trust = 100.0
        
        device = self.pip.getDeviceByMAC(MAC)

        # Dispositivo nunca utilizado
        if not device:
            trust -= 60

        # Dispositivo compartilhado por outros usuários
        if device:
            usersIndex = []
            deviceUse = self.pip.getAcessHistoricByDevice(MAC, date)
            for use in deviceUse:
                if use[0] not in usersIndex:
                    usersIndex.append(use[0])
            if len(usersIndex) > 1 and len(usersIndex) <= 3:
                trust -= 30
            elif len(usersIndex) > 3:
                trust -= 50

        # Alterações nas características do dispositivo (device finger print)
        if device:
            idCDB, dfpDB, osDB, versionOsDB, dateDB,statusDB, idD1DB, idD2DB, macDB = self.pip.getDeviceByMAC(MAC)
            if (dfpDB != dfp) or (osDB != os) or (versionOsDB != versionOs):
                trust -= 20
                self.pip.updateDeviceCharacteristic(MAC, dfp, os, versionOs, date)

        # Dispositivo com verção de sistema menos seguros


        if trust > 0:
            return trust
        return 0

    # Avalia o histórico de acesso do usuário
    def __evaluateUserHistory(self, registry) -> float:

        # Média da confiança das ultimas X requisições
        trust = self.pip.getAverageTrustAccess(registry)

        # Frequência de acesso à recursos altamente sinsíveis

        # Multiplas requisições negadas

        return trust

    # Define a sensibilidade do recurso acessado
    def __evaluateResourceSensibility(self) -> float:
        logging.info("Evaluate resource sensibility")