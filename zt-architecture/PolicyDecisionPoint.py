import logging
import response


class PolicyDecisionPoint:

    def policyAdministrator(self, conn, addr, data):
        print(data)
        return response.ACCESS_ALLOWED

    def policyEngine(self):
        logging.info("policy Engine")

    # Realiza login do usuário
    def __login(self):
        logging.info("Login")

    # Realiza reautenticação do usuário
    def __reauthenticate(self):
        logging.info("Reauthenticate")

    # Valida se o usuário está devidamente autenticado
    def __checkUserCredentials(self):
        logging.info("Evaluate user credentials")
    
    # Valida se o usuário possui permissão para acesso o recurso desejado
    def __checkUserPermissions(self):
        logging.info("evaluate user permissions")
    
    # Avalia o dispositivo utilizado pelo usuário
    def __evaluateUserDevice(self):
        logging.info("evaluate user device")

    # Avalia os atributos do usuário
    def __evaluateUserAtributesAndContext(self):
        logging.info("Evaluate user atributes")

    # Avalia o histórico de acesso do usuário
    def __evaluateUserHistory(sef):
        logging.info("evaluate user history")

    # Define a sensibilidade do recurso acessado
    def __evaluateResourceSensibility(self):
        logging.info("Evaluate resource sensibility")