from decouple import config
import mysql.connector


MYSQL_HOST = config('MYSQL_HOST')
MYSQL_USER = config('MYSQL_USER')
MYSQL_PASS = config('MYSQL_PASS')

def dbConnect():
  return mysql.connector.connect(
  host=MYSQL_HOST,
  user=MYSQL_USER,
  password=MYSQL_PASS
)