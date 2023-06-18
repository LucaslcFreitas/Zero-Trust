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

x_dataAllowedNormal = []
y_dataAllowedNormal = []
x_dataAllowedReauthenticate = []
y_dataAllowedReauthenticate = []
x_dataDeniedNormal = []
y_dataDeniedNormal = []
x_dataDeniedReauthenticate = []
y_dataDeniedReauthenticate = []
x_sensibility = []
y_sensibility = []
for access in accessList:
    x_sensibility.append(access[9])
    y_sensibility.append(access[15])
    if access[10] == 'Permitido' and access[14] == False:
        x_dataAllowedNormal.append(access[9])
        y_dataAllowedNormal.append(access[12])
    elif access[10] == 'Permitido' and access[14] == True:
        x_dataAllowedReauthenticate.append(access[9])
        y_dataAllowedReauthenticate.append(access[12])
    elif access[14] == False:
        x_dataDeniedNormal.append(access[9])
        y_dataDeniedNormal.append(access[12])
    else:
        x_dataDeniedReauthenticate.append(access[9])
        y_dataDeniedReauthenticate.append(access[12])

plt.plot(x_sensibility, y_sensibility, color='gray', linewidth=1.8, zorder=1)
plt.scatter(x_dataAllowedNormal, y_dataAllowedNormal, color='green', s=70, zorder=2)
plt.scatter(x_dataAllowedReauthenticate, y_dataAllowedReauthenticate, color='blue', s=70, zorder=2)
plt.scatter(x_dataDeniedNormal, y_dataDeniedNormal, color='red', s=70, zorder=2)
plt.scatter(x_dataDeniedReauthenticate, y_dataDeniedReauthenticate, color='orange', s=70, zorder=2)
plt.ylim(0, 100)

# for i in range(len(x_dataAllowed)):
#     plt.text(x_dataAllowed[i], y_dataAllowed[i], str(y_dataAllowed[i]), ha='center', va='bottom')


date_formatter = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gca().xaxis.set_major_formatter(date_formatter)

plt.gcf().autofmt_xdate()

plt.xlabel('Tempo', fontsize=16)
plt.ylabel('Confiança/Sensibilidade', fontsize=16)
plt.title('Dispositivo com Baixa Segurança 3', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()