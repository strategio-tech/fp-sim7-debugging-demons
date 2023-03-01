import os
from decouple import config
import mysql.connector

MYSQL_HOST = config('MYSQL_HOST')
MYSQL_USER = config('MYSQL_USER')
MYSQL_PASS = config('MYSQL_PASS')
MYSQL_DATABASE = config('MYSQL_DATABASE')

def dbConnect(setup = False):

  if setup:
    return mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASS
    )

  return mysql.connector.connect(
    database=MYSQL_DATABASE,
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASS
  )