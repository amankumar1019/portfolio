import mysql.connector
import json

with open('config.json') as json_data:
    d = json.load(json_data)
    json_data.close()

DB_PARAMS = d.get("DB_PARAMS")
host = DB_PARAMS.get("host")
user = DB_PARAMS.get("user")
password=DB_PARAMS.get("password")
database_name = DB_PARAMS.get("database")

mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database=database_name
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM contact")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)