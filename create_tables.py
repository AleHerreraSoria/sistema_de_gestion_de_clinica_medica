# create_tables.py
from database import engine, Base
import models

print("Creando tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("¡Proceso de creación de tablas finalizado!")