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

x_dataAllowed = []
y_dataAllowed = []
x_dataDenied = []
y_dataDenied = []
x_sensibility = []
y_sensibility = []
for access in accessList:
    x_sensibility.append(access[9])
    y_sensibility.append(access[14])
    if access[10] == 'Permitido':
        x_dataAllowed.append(access[9])
        y_dataAllowed.append(access[12])
    else:
        x_dataDenied.append(access[9])
        y_dataDenied.append(access[12])



plt.plot(x_sensibility, y_sensibility, color='yellow')
plt.scatter(x_dataAllowed, y_dataAllowed, color='blue')
plt.scatter(x_dataDenied, y_dataDenied, color='red')
plt.ylim(0, 100)


date_formatter = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gca().xaxis.set_major_formatter(date_formatter)

plt.gcf().autofmt_xdate()

plt.xlabel('Tempo')
plt.ylabel('Confiança')
plt.title('Gráfico de Acesso do Usuário: '+userRegistry)

plt.show()