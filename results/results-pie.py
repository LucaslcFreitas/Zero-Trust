import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import psycopg2
import json
import os
import pytz

with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json") as file:
    config = json.load(file)

connection = psycopg2.connect(
    host=config["dbHost"],
    port=config["dbPort"],
    database=config["dbDatabase"],
    user=config["dbUser"],
    password=config["dbPassword"]
)

userRegistry = "460.395.930-32"

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT ac.*, se.sensibilidade FROM \"zt-ehealth\".\"Acesso\" AS ac INNER JOIN (SELECT atP.id AS ipt, atS.* FROM \"zt-ehealth\".\"Permissao\" AS atP INNER JOIN \"zt-ehealth\".\"SensibilidadeSubRecurso\" AS atS ON atP.\"idSubRecurso\" = atS.\"idSubRecurso\" AND atp.\"tipoAcao\" = ats.\"tipoAcao\") AS se ON ac.\"idPermissao\" = se.ipt WHERE ac.\"idUsuario\" = (SELECT id FROM \"zt-ehealth\".\"Usuario\" WHERE cpf = '"+userRegistry+"') AND resultado <> 'Reautenticacao' ORDER BY data ASC")
        result = cursor.fetchall()
        if result:
            accessList = result
        else:
            exit()
except Exception as e:
    print(e)
    exit()

def formatar_porcentagem(valor):
    if valor == 0:
        return ''
    else:
        return f'{valor:.1f}%'

data = [0, 0, 0, 0]
labels = ["Permitido", "Permitido com reautenticação", "Negado", "Negado por falta de reautenticação"]
colors = ['green', 'blue', 'red', 'orange']

brasil_tz = pytz.timezone('America/Sao_Paulo')
for access in accessList:
    if access[10] == 'Permitido' and access[14] == False:
        data[0] += 1
    elif access[10] == 'Permitido' and access[14] == True:
        data[1] += 1
    elif access[14] == False:
        data[2] += 1
    else:
        data[3] += 1


plt.pie(data, colors=colors, autopct=formatar_porcentagem)

plt.title('Gráfico em Pizza')

plt.show()


