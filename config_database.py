import pymysql # UNICAMENTE MySQL
import psycopg2
from sqlalchemy import create_engine
import pandas as pd


conexion = pymysql.connect(
    database='car_company',
    host='localhost',
    port=3307,
    user='root',
    passwd='dragonroot'
)
cursor = conexion.cursor()
if conexion:
    print('CONEXION EXITOSA!!!')


conexion.close() 


