import psycopg2
import os
import json

with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json") as file:
    config = json.load(file)

conn = psycopg2.connect(
    host=config["dbHost"],
    port=config["dbPort"],
    database=config["dbDatabase"],
    user=config["dbUser"],
    password=config["dbPassword"]
)
cursor = conn.cursor()

with open(os.path.dirname(os.path.abspath(__file__)) + '/reset.sql') as resetFile:
    script = resetFile.read()

cursor.execute(script)

conn.commit()
conn.close()