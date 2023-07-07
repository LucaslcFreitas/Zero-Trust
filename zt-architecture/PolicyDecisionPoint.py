import logging
import json
import datetime
import random
import hashlib
import ipaddress
import math
import os as oss
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
                    return self.__login(data['REGISTRY'], data['PASSWORD'], data['TIME'])
            case TypeRequest.ACCESS:
                if (data['RESOURCE'] and data['SUB_RESOURCE'] and data['TYPE_ACTION'] and data['TOKEN'] and data['IP_ADDRESS'] and data['LATITUDE'] and data['LONGITUDE'] and data['MAC'] and data['DFP'] and data['OS'] and data['VERSION_OS'] and data['TIME']):
                    return self.policyEngine(data)
                return Response.ACCESS_DENIED, None
            case TypeRequest.UPDATE_PASSWORD:
                if (data['TOKEN'] and data['OLD_PASSWORD'] and data['NEW_PASSWORD'] and data['IP_ADDRESS'], data['LATITUDE'] and data['LONGITUDE'] and data['MAC'] and data['DFP'] and data['OS'] and data['VERSION_OS'] and data['TIME']):
                    return self.__updatePassword(data['TOKEN'], data['OLD_PASSWORD'], data['NEW_PASSWORD'], data['TIME'])
            case TypeRequest.REAUTHENTICATION:
                if (data['TOKEN'] and data['REGISTRY'] and data['PASSWORD'] and data['IP_ADDRESS'] and data['LATITUDE'] and data['LONGITUDE'] and data['MAC'] and data['DFP'] and data['OS'] and data['VERSION_OS'] and data['TIME'] and data['ID_ACCESS']):
                    return self.__reauthenticate(data['TOKEN'], data['REGISTRY'], data['PASSWORD'], data['TIME'], data['ID_ACCESS'], data['MAC'], data['DFP'], data['OS'], data['VERSION_OS'], data['IP_ADDRESS'], data['LATITUDE'], data['LONGITUDE'])
            case _: # Default
                return Response.ACCESS_DENIED, None

    def policyEngine(self, data):
        # Verifica se o usuário está devidamente autenticado
        if not self.__checkUserCredentials(data['TOKEN'], data['TIME']):
            #registrar acesso negado...
            return Response.AUTHENTICATION_REQUIRED, None

        # Pega as credênciais do usuário
        user = self.pip.getUserAttributes(data['TOKEN'])

        # Verifica se o recurso e subrecurso existe, caso contrário o acesso é nogado e registrado com confiança mínima
        resource = self.pip.getSubResourceSocketByName(data['RESOURCE'], data['SUB_RESOURCE'])
        if not resource:
            self.pip.registerAccessDeniedOrReauthenticated(user['registry'], data['TOKEN'], data['LATITUDE'], data['LONGITUDE'], data['TIME'], data['IP_ADDRESS'], "Negado", 5, data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'], idDeviceTMP)
            return Response.RESOURCE_NOT_FOUND, None

        # Verifica se o usuário possui permissão para acessar o recurso, caso contrário o acesso é nogado e registrado com confiança mínima
        if not self.pip.checkResourceUserPermissions(data['TOKEN'], data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'], data['TIME']):
            self.pip.registerAccessDeniedOrReauthenticated(user['registry'], data['TOKEN'], data['LATITUDE'], data['LONGITUDE'], data['TIME'], data['IP_ADDRESS'], "Negado", 5, data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'], idDeviceTMP)
            return Response.ACCESS_DENIED, None

        try:
            # Calcula a confiança com base no contexto
            userTrust = self.__evaluateContext(user['registry'], data['TIME'], data['LATITUDE'], data['LONGITUDE'], data['IP_ADDRESS'], user['type'])
        
            # Calcula a confiança com base no dispositivo
            deviceTrust = self.__evaluateDevice(data['MAC'], data['DFP'], data['OS'], data['VERSION_OS'], data['TIME'])
        
            # Calcula a confiança com base no histórico de acesso
            historyTrust = self.__evaluateHistory(user['registry'], data['TIME'])

            # Pega a sensibilidade do recurso
            sensitivity = self.pip.getResourceSensibilityByName(data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'])
        except Exception as e:
            return Response.INTERNAL_SERVER_ERROR, None

        # Calcula a confinça final
        trust = 0
        if historyTrust == 0:
            trust = math.sqrt(userTrust * deviceTrust) * 0.1
        else:
            trust = math.sqrt(userTrust * deviceTrust) * (historyTrust/100)

        # Decisão final
        result = None
        if (trust >= 0 and trust < 50) and (sensitivity >= 0 and sensitivity < 25):
            result = Response.REAUTHENTICATION_REQUIRED
        elif (trust >= 25 and trust < 50) and (sensitivity >= 0 and sensitivity < 75):
            result = Response.REAUTHENTICATION_REQUIRED
        elif (trust >= 50 and trust < 75) and (sensitivity >= 50):
            result = Response.REAUTHENTICATION_REQUIRED
        elif (trust >= 0 and trust < 25) and (sensitivity >= 25):
            result = Response.ACCESS_DENIED
        elif (trust >= 25 and trust < 50) and (sensitivity >= 75):
            result = Response.ACCESS_DENIED
        elif (trust >= 50 and trust < 75) and (sensitivity >= 0 and sensitivity < 50):
            result = Response.ACCESS_ALLOWED
        elif (trust >= 75):
            result = Response.ACCESS_ALLOWED
        
        match (result):
            case Response.REAUTHENTICATION_REQUIRED:
                idDeviceTMP = self.__registerDeviceForAccessDeniedOrReauthenticated(data['MAC'], data['DFP'], data['OS'], data['VERSION_OS'], data['TIME'])
                if idDeviceTMP:
                    idAccess =  self.pip.registerAccessDeniedOrReauthenticated(user['registry'], data['TOKEN'], data['LATITUDE'], data['LONGITUDE'], data['TIME'], data['IP_ADDRESS'], "Reautenticacao", trust, data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'], idDeviceTMP)
                    if idAccess:
                        return result, {"idAccess": idAccess}
                return Response.INTERNAL_SERVER_ERROR, None
            case Response.ACCESS_DENIED:
                idDeviceTMP = self.__registerDeviceForAccessDeniedOrReauthenticated(data['MAC'], data['DFP'], data['OS'], data['VERSION_OS'], data['TIME'])
                if idDeviceTMP:
                    idAccess =  self.pip.registerAccessDeniedOrReauthenticated(user['registry'], data['TOKEN'], data['LATITUDE'], data['LONGITUDE'], data['TIME'], data['IP_ADDRESS'], "Negado", trust, data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'], idDeviceTMP)
                    if idAccess:
                        return result, None
                return Response.INTERNAL_SERVER_ERROR, None
            case Response.ACCESS_ALLOWED:
                self.__registerOrUpdateDevice(data['MAC'], data['DFP'], data['OS'], data['VERSION_OS'], data['TIME'])
                idAccess =  self.pip.registerAccess(user['registry'], data['TOKEN'], data['LATITUDE'], data['LONGITUDE'], data['MAC'], data['TIME'], data['IP_ADDRESS'], "Permitido", trust, data['RESOURCE'], data['SUB_RESOURCE'], data['TYPE_ACTION'])
                if idAccess:
                    return result, resource
                return Response.INTERNAL_SERVER_ERROR, None
        
        return Response.INTERNAL_SERVER_ERROR, None

    # Realiza login do usuário
    def __login(self, registry, password, date) -> str:
        pswToken = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        auxUserToken = registry + password + str(datetime.datetime.now()) + str(random.randint(1, 100000))
        userToken = hashlib.sha256(str(auxUserToken).encode('utf-8')).hexdigest()
        validity = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(hours=3)
        result = 'Negado'

        if self.pip.checkLogin(registry, pswToken):
            result = 'Permitido'

        self.pip.registerLoginAndToken(registry, pswToken, date, result, userToken, validity)
        if result == 'Permitido':
            return Response.AUTHORIZED_LOGIN, {"token": userToken}
        return Response.ACCESS_DENIED, None
    
    # Realiza autalização de senha do usuário
    def __updatePassword(self, token, oldPsw, newPsw, date):
        oldPswToken = hashlib.sha256(str(oldPsw).encode('utf-8')).hexdigest()
        if self.__checkUserCredentials(token, date):
            user = self.pip.getUserAttributes(token)
            newPswToken = hashlib.sha256(str(newPsw).encode('utf-8')).hexdigest()
            auxUserToken = user["registry"] + newPsw + str(datetime.datetime.now()) + str(random.randint(1, 100000))
            newUserToken = hashlib.sha256(str(auxUserToken).encode('utf-8')).hexdigest()
            validity = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(hours=3)
            if self.pip.checkPasswordValidity(user["registry"], oldPswToken):
                if self.pip.updatePassword(user["registry"], newPswToken, date):
                    if self.pip.registerLoginAndToken(user["registry"], newPswToken, date, 'Permitido', newUserToken, validity):
                        return Response.UPDATED_PASSWORD, {"token": newUserToken}
            else:
                self.pip.registerLoginAndToken(user["registry"], newPswToken, date, 'Negado', newUserToken, validity)
        return Response.UNAUTHORIZED_PASSWORD_UPDATE, None

    # Realiza reautenticação do usuário
    def __reauthenticate(self, token, registry, password, date, idAccess, MAC, dfp,os, versionOs, ip, latitude, longitude):
        if  self.__checkUserCredentials(token, date):
            access = self.pip.getAccessById(idAccess)

            # Compara atributos atuais em relação ao acesso de reautenticação
            deviceAccess = self.pip.getDeviceTMPById(access[13])
            if deviceAccess[1] != MAC or deviceAccess[2] != dfp or deviceAccess[3] != os or deviceAccess[4] != versionOs:
                return Response.ACCESS_DENIED, None
            if access[11] != ip:
                return Response.ACCESS_DENIED, None
            distance = geodesic((latitude, longitude), (access[7], access[8])).meters
            if distance >= 4200:
                return Response.ACCESS_DENIED, None
            currentDate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3)))
            diferenceTime = currentDate - access[9]
            if diferenceTime > datetime.timedelta(minutes=5):
                return Response.ACCESS_DENIED, None

            resp, body = self.__login(registry, password, date)
            if resp == Response.AUTHORIZED_LOGIN and body["token"]:
                resource = self.pip.getResourceSocketBySubResourceId(access[4])
                if resource:
                    self.__registerOrUpdateDevice(MAC, dfp, os, versionOs, date)
                    newAccess =  self.pip.registerAccessAllowedForReauthenticate(access[1], body["token"], access[3], access[4], access[5], MAC, access[7], access[8], date, "Permitido", ip, access[12])
                    if newAccess:
                        resp = {
                        'ipAddress': resource['ipAddress'],
                        'port': resource['port'],
                        'token': body['token']
                    }
                        return Response.REAUTHENTICATION_ALLOWED, resp
        return Response.ACCESS_DENIED, None
    
    # Registra negação de acesso por falta de reautenticação
    def registerDeniedForNotReauthentication(self, idAccess):
        access = self.pip.getAccessById(idAccess)
        if access:
            self.pip.registerAccessDeniedForReauthenticate(access[1], access[2], access[3], access[4], access[5], access[7], access[8], access[9], "Negado", access[11], access[12], access[13])

    # Valida se o usuário está devidamente autenticado
    def __checkUserCredentials(self, token, date):
        if not len(token) == 64:
            return False
        
        return self.pip.checkTokenValidity(token, date)
    
    # Avalia os atributos do usuário
    def __evaluateContext(self, registry, date, latitude, longitude, ip, typeUser) -> float:
        trust = 100.0
        
        # Avalia logins recentes
        recentLogins = self.pip.getRegLoginDeniedHistory(registry, date)
        countFailedLogins = 0
        if recentLogins:
            for login in recentLogins:
                if login[1] == 'Negado':
                    countFailedLogins += 1
        if countFailedLogins >= 1 and countFailedLogins < 4:
            trust -= 35
        elif countFailedLogins >= 4 and countFailedLogins < 7:
            trust -= 47
        elif countFailedLogins >= 7:
            trust -= 60
        

        # Avalia troca de senhas recentes
        recentPasswordChanges = self.pip.getUserPasswordHistory(registry, date)
        countPasswordChanges = 0
        if recentPasswordChanges:
            countPasswordChanges = len(recentPasswordChanges)
        if countPasswordChanges >= 1 and countPasswordChanges < 3:
            trust -= 10
        elif countPasswordChanges >= 3 and countPasswordChanges < 6:
            trust -= 20
        elif countPasswordChanges >= 6:
            trust -= 30
        
        # Avalia mudanca consideravel na localizacao recente
        recentLocations = self.pip.getRecentLocationAccessUser(registry, date) # Avaliação com base nos acessos recentes, para detectar mudanças bruscas na localização
        baseLocations = self.pip.getHistoryLocationAccessUser(registry, date) # Avaliação da base de acesso do ultimo mês, para detectar acesso fora da região de costume
        if recentLocations:
            maxDiference = 0
            for recenteLoc in recentLocations:
                timeR = ((datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - recenteLoc[2]).total_seconds() / 60) / 60 # Diferença do tempo atual em relação ao acesso, normalizado (0, 1)
                distanceR = geodesic((latitude, longitude), (recenteLoc[0], recenteLoc[1])).meters
                diferenceR = distanceR / (timeR * 30000)
                if diferenceR > maxDiference:
                    # print(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))))
                    # print(recenteLoc[2])
                    maxDiference = diferenceR
            
            if (maxDiference > 1 and maxDiference < 1.3):
                trust -= 30
            elif (maxDiference >= 1.3 and maxDiference < 1.5):
                trust -= 42
            elif (maxDiference >= 1.5 and maxDiference < 2.0):
                trust -= 55
            elif maxDiference >= 2.0:
                trust -= 68
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
                    trust -= 20
            else:
                trust -= 40
        else:
            trust -= 40
        

        # Avalia horário de acesso
        if typeUser == 'Profissional':
            employeeAttributes = self.pip.getEmployeeAttributes(registry)
            hoursOut = 0
            nDate = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            daysWord = employeeAttributes["workDays"].split("-")
            auxHs1 = datetime.datetime.combine(nDate, employeeAttributes["wrokStart"])
            auxHs2 = datetime.datetime.combine(nDate, employeeAttributes["workEnd"])
            if auxHs1 > auxHs2:
                if nDate > auxHs1:
                    auxHs2 = auxHs2 + datetime.timedelta(days=1)
                elif nDate < auxHs2:
                    auxHs1 = auxHs1 - datetime.timedelta(days=1)
            
            if nDate >= auxHs1 and nDate <= auxHs2 and auxHs1.strftime("%A") in daysWord:
                hoursOut = 0
            else:
                if auxHs1.day != auxHs2.day:
                    while (auxHs2 - datetime.timedelta(days=1)).strftime("%A") not in daysWord:
                        auxHs2 = auxHs2 - datetime.timedelta(days=1)
                else:
                    while auxHs2.strftime("%A") not in daysWord:
                        auxHs2 = auxHs2 - datetime.timedelta(days=1)
                    
                while auxHs1.strftime("%A") not in daysWord:
                    auxHs1 = auxHs1 + datetime.timedelta(days=1)
                
                if auxHs1 > nDate:
                    auxT1 = auxHs1 - nDate
                else:
                    auxT1 = nDate - auxHs1
                if auxHs2 > nDate:
                    auxT2 = auxHs2 - nDate
                else:
                    auxT2 = nDate - auxHs2
                if auxT1 < auxT2:
                    hoursOut = auxT1.total_seconds() / 3600
                else:
                    hoursOut = auxT2.total_seconds() / 3600
            
            if hoursOut > 0 and hoursOut <= 1:
                trust -= 20
            elif hoursOut > 1 and hoursOut <= 3:
                trust -= 40
            elif hoursOut > 3 and hoursOut <= 6:
                trust -= 50
            elif hoursOut > 6:
                trust -= 68

        # Avalia reduções de privilégios recentes
        reducedPrivileges = self.pip.getRecentReducedPrivilege(registry, date)
        if reducedPrivileges:
            for privilege in reducedPrivileges:
                if privilege[0] == 'Inativo':
                    trust -= 10

        # Avalia uso de rede de acesso recente
        networkUses = self.pip.getRecentNetworkUse(registry, date)
        networkUser = ipaddress.ip_interface(ip)
        auxNetWorks = {}
        if networkUses:
            for histNet in networkUses:
                auxNetH = ipaddress.ip_interface(histNet[0])
                if str(auxNetH.network) in auxNetWorks:
                    auxNetWorks[str(auxNetH.network)] += 1
                else:
                    auxNetWorks[str(auxNetH.network)] = 1
        if str(networkUser.network) != '172.16.10.0/24' and (not str(networkUser.network) in auxNetWorks):
            trust -= 50
        elif str(networkUser.network) != '172.16.10.0/24' and str(networkUser.network) in auxNetWorks:
            if auxNetWorks[str(networkUser.network)] < 3:
                trust -= 50
            elif auxNetWorks[str(networkUser.network)] >= 3 and auxNetWorks[str(networkUser.network)] < 7:
                trust -= 25

        if trust > 0:
            return trust
        return 0.1

    # Avalia o dispositivo utilizado
    def __evaluateDevice(self, MAC, dfp, os, versionOs, date) -> float:
        trust = 100.0
        
        device = self.pip.getDeviceByMAC(MAC)

        # Dispositivo compartilhado por outros usuários
        if device:
            usersIndex = []
            deviceUse = self.pip.getAcessHistoricByDevice(MAC, date)
            if deviceUse:
                for use in deviceUse:
                    if use[9] == 'Permitido' and use[0] not in usersIndex:
                        usersIndex.append(use[0])
            if len(usersIndex) > 1 and len(usersIndex) <= 3:
                trust -= 25
            elif len(usersIndex) > 3:
                trust -= 40

        # Alterações nas características do dispositivo (device finger print)
        if device:
            idCDB, dfpDB, osDB, versionOsDB, dateDB,statusDB, idD1DB, idD2DB, macDB = self.pip.getDeviceByMAC(MAC)
            if (dfpDB != dfp) or (osDB != os) or (versionOsDB != versionOs):
                trust -= 70

        # Dispositivo com verção de sistema menos seguros
        with open(oss.path.dirname(oss.path.abspath(__file__)) + "/deviceVersionRisk.json") as file:
            deviceRisks = json.load(file)
            if deviceRisks:
                unknownRisk = True
                for deviceRisk in deviceRisks:
                    if os == deviceRisk["Operational System"] and versionOs == deviceRisk["Version"]:
                        match (deviceRisk["Risk"]):
                            case "medium":
                                trust -= 18
                            case "high":
                                trust -= 26
                            case "unacceptably high":
                                trust -= 38
                        unknownRisk = False
                        break
                if unknownRisk:
                    trust -= 38

        # Dispositivo recente ou nunca utilizado
        numberAccess = self.pip.getNumberAccessByDevice(MAC)
        if not numberAccess or numberAccess == 0:
            trust -= 60
        elif numberAccess >= 1 and numberAccess < 9:
            trust -= 40
        elif numberAccess >= 9 and numberAccess < 15:
            trust -= 30
        elif numberAccess >= 15 and numberAccess < 23:
            trust -= 15
        
        if trust > 0:
            return trust
        return 0.1

    # Avalia o histórico de acesso
    def __evaluateHistory(self, registry, date) -> float:
        trust = 100

        # Avalia quantidade de acessos
        numberAccess = self.pip.getNumberAccessByUser(registry)
        if not numberAccess:
            numberAccess = 0
        if numberAccess < 10:
            trust -= 40
        elif numberAccess < 25:
            trust -= 20
        elif numberAccess < 35:
            trust -= 10

        historyWithSensibility = self.pip.getAccessHistoryWithSensibility(registry, date)

        # Frequência de acesso recente à recursos altamente sinsíveis
        if historyWithSensibility:
            countHighlySensitive = 0
            timeLimit = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))) - datetime.timedelta(hours=3)
            for hs in historyWithSensibility:
                if hs[15] >= 75 and hs[9] > timeLimit:
                    countHighlySensitive += 1
            if countHighlySensitive >= 5 and countHighlySensitive < 8:
                trust -= 12
            elif countHighlySensitive >= 8 and countHighlySensitive < 11:
                trust -= 20
            elif countHighlySensitive >= 11:
                trust -= 28

        # Multiplas requisições negadas (verificar restrição de data)
        if historyWithSensibility:
            countDeniAccess = 0
            for hs in historyWithSensibility:
                if hs[10] == "Negado":
                    countDeniAccess += 1
            if countDeniAccess >= 3 and countDeniAccess < 8:
                trust -= 15
            elif countDeniAccess >= 8 and countDeniAccess < 12:
                trust -= 30
            elif countDeniAccess >= 12 and countDeniAccess < 15:
                trust -= 55
            elif countDeniAccess >= 15:
                trust -= 70
        
        # Média da confiança calculada com a média do histórico
        avgTrust = self.pip.getAverageTrustLastAccess(registry)
        
        if not avgTrust:
            avgTrust = 0
        trust = (trust + avgTrust) / 2

        if trust > 0:
            return trust
        return 0
    
    def __registerOrUpdateDevice(self, MAC, dfp, os, versionOs, date):
        device = self.pip.getDeviceByMAC(MAC)
        if device:
            idCDB, dfpDB, osDB, versionOsDB, dateDB, statusDB, idD1DB, idD2DB, macDB = device
            if (dfpDB != dfp) or (osDB != os) or (versionOsDB != versionOs):
                self.pip.updateDeviceCharacteristic(MAC, dfp, os, versionOs, date)
        else:
            self.pip.registerDevice(MAC, dfp, os, versionOs, date)

    def __registerDeviceForAccessDeniedOrReauthenticated(self, MAC, dfp, os, versionOs, date):
        return self.pip.registerDeviceTMP(MAC, dfp, os, versionOs, date)