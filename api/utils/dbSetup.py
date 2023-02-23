from dbConnect import dbConnect
from decouple import config
import requests

MYSQL_DATABASE = config('MYSQL_DATABASE')

mydb = dbConnect(setup=True)
cursor = mydb.cursor()

cursor.execute(f"CREATE DATABASE {MYSQL_DATABASE}")

mydb = dbConnect()
cursor = mydb.cursor()

cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user VARCHAR(255), password VARCHAR(255))")
cursor.execute("CREATE TABLE history (id INT AUTO_INCREMENT PRIMARY KEY, prompt VARCHAR(255))")