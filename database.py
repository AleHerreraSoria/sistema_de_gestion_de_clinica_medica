# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ATENCIÓN: Reemplaza 'tu_contraseña' con tu contraseña real de PostgreSQL
DATABASE_URL = "postgresql://postgres:proyecto2025@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()