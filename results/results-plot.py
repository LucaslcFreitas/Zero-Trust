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
brasil_tz = pytz.timezone('America/Sao_Paulo')
for access in accessList:
    # if access[9] >= datetime.datetime.strptime("2023-06-15 13:35:00.047062", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))): # instance C5
    # if access[9] >= datetime.datetime.strptime("2023-06-15 16:00:00.047062", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3))): # instance C6
    if True:
        x_sensibility.append(access[9] - datetime.timedelta(hours=3))
        y_sensibility.append(access[15])
        if access[10] == 'Permitido' and access[14] == False:
            x_dataAllowedNormal.append(access[9] - datetime.timedelta(hours=3))
            y_dataAllowedNormal.append(access[12])
        elif access[10] == 'Permitido' and access[14] == True:
            x_dataAllowedReauthenticate.append(access[9] - datetime.timedelta(hours=3))
            y_dataAllowedReauthenticate.append(access[12])
        elif access[14] == False:
            x_dataDeniedNormal.append(access[9] - datetime.timedelta(hours=3))
            y_dataDeniedNormal.append(access[12])
        else:
            x_dataDeniedReauthenticate.append(access[9] - datetime.timedelta(hours=3))
            y_dataDeniedReauthenticate.append(access[12])

plt.plot(x_sensibility, y_sensibility, color='gray', linewidth=1.8, zorder=1)
plt.scatter(x_dataAllowedNormal, y_dataAllowedNormal, color='green', s=70, zorder=2)
plt.scatter(x_dataAllowedReauthenticate, y_dataAllowedReauthenticate, color='blue', s=70, zorder=2)
plt.scatter(x_dataDeniedNormal, y_dataDeniedNormal, color='red', s=70, zorder=2)
plt.scatter(x_dataDeniedReauthenticate, y_dataDeniedReauthenticate, color='orange', s=70, zorder=2)
plt.ylim(0, 100)


date_formatter = mdates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(date_formatter)
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

plt.gcf().autofmt_xdate()
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
plt.xlabel('Tempo', fontsize=16)
plt.ylabel('Confiança/Sensibilidade', fontsize=16)
plt.title('Acessos', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()