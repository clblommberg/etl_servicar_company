from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # Importación actualizada
from models import *  # Importa tus modelos SQLAlchemy aquí

DATABASE_URL = "sqlite:///car_company.db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()  # Base declarativa

def init_db():
    Base.metadata.create_all(engine)  # Crear todas las tablas

if __name__ == "__main__":
    init_db()