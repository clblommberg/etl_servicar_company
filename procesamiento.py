"""import pandas as pd
import os
ruta_actual = os.getcwd()
ruta_relativa = os.path.join(ruta_actual, 'dataset.xlsx')
df = pd.read_excel('data/raw/dataset.xlsx', sheet_name='BD CONVERSIONES')
print(df.head(5))
"""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base
from models import Base, Inventario, VehiculosCliente, Productos, Conversion  # Importa las tablas desde models.py


# Leer el DataFrame desde un archivo CSV o fuente de datos
df = pd.read_excel('data/raw/dataset.xlsx', sheet_name='BD CONVERSIONES')

# Limpieza de datos:
# - Corregir mayúsculas/minúsculas en columnas
# - Corregir valores faltantes
# - Convertir tipos de datos

# Ejemplo: transformar FECHA a tipo Date
df['FECHA'] = pd.to_datetime(df['FECHA'])

# ... agregar más operaciones de limpieza según sea necesario

# Imprimir el DataFrame limpio
print(df.head())

# Conexión a la base de datos SQLite
engine = create_engine("sqlite:///car_company.db")  # Cambia la URL de la base de datos SQLite
Session = sessionmaker(bind=engine)
session = Session()

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Iterar sobre las filas del DataFrame y crear objetos de cada tabla
for index, row in df.iterrows():
    # Mapear fila del DataFrame a un objeto de cada tabla
    vehiculo = VehiculosCliente(nombrecliente=row["MARCA / MODELO"], Placa=row["PLACA"], Ubicacion=row["UBICACIÓN"])
    # ... crear objetos para otras tablas con los datos correspondientes
    session.add_all([vehiculo])

# Guardar los cambios en la base de datos
session.commit()

# Imprimir mensaje de confirmación
print("¡Datos migrados exitosamente a SQLite!")
