from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Inventario(Base):
    __tablename__ = 'Inventario'
    idinventario = Column(Integer, primary_key=True)
    stock_inicial = Column(Integer)
    stock_actual = Column(Integer)
    stock_final = Column(Integer)

class VehiculosCliente(Base):
    __tablename__ = 'Vehiculoscliente'
    idvehiculo = Column(Integer, primary_key=True)
    nombrecliente = Column(String(100))
    Marca_Modelo = Column(String(100))
    Placa = Column(String(20))

class Lnegocio(Base):
    __tablename__ = 'Lnegocio'
    idlinea = Column(Integer, primary_key=True)
    linea_negocio = Column(String(100))

class Conversion(Base):
    __tablename__ = 'Conversion'
    idconversion = Column(Integer, primary_key=True)
    nconversion = Column(String(50))
    galones = Column(Integer)
    idinventario = Column(Integer, ForeignKey('Inventario.idinventario'))

class Aplicacion(Base):
    __tablename__ = 'Aplicacion'
    idaplicacion = Column(Integer, primary_key=True, autoincrement=True)
    aplicacion_name = Column(String(50))

class Servicios(Base):
    __tablename__ = 'Servicios'
    idservicio = Column(Integer, primary_key=True, autoincrement=True)
    Descripcion = Column(String(100))
    Precio = Column(DECIMAL(10, 2))

class Kit(Base):
    __tablename__ = 'Kit'
    idkit = Column(Integer, primary_key=True)
    clasekit= Column(Integer)
    kitmarca = Column(String(50))
    tecnologia = Column(Integer)
    idinventario = Column(Integer, ForeignKey('Inventario.idinventario'))

class Transacciones(Base):
    __tablename__ = 'Transacciones'
    idtrasaccion = Column(Integer, primary_key=True)
    Fecha = Column(Date)
    documento = Column(String(100))
    idvehiculo = Column(Integer, ForeignKey('Vehiculoscliente.idvehiculo'))
    idproducto = Column(Integer, ForeignKey('Lnegocio.idlinea'))
    valida_certificado = Column(Integer)
    costotanque = Column(DECIMAL(10, 2))
    costokit = Column(DECIMAL(10, 2))
    costocertificacion = Column(DECIMAL(10, 2))
    precioventa = Column(DECIMAL(10, 2))
    Ganancia = Column(DECIMAL(10, 2))
    idconversion = Column(Integer, ForeignKey('Conversion.idconversion'))
    idkit = Column(Integer, ForeignKey('Kit.idkit'))
    idaplicacion = Column(Integer, ForeignKey('Aplicacion.idaplicacion'))

class Pagos(Base):
    __tablename__ = 'Pagos'
    idpago = Column(Integer, primary_key=True, autoincrement=True)
    idtrasanccion = Column(Integer, ForeignKey('Transacciones.idtrasaccion'))
    Efectivo = Column(DECIMAL(10, 2))
    BCP = Column(DECIMAL(10, 2))
    Tarjeta = Column(DECIMAL(10, 2))
