# gestion_profesionales.py

from database import SessionLocal
from models import Profesional
from sqlalchemy import text # Importamos text para SQL directo

# --- MÉTODO 1: Usando el ORM de SQLAlchemy ---
# Ventajas: Más seguro (previene inyección SQL), más legible y orientado a objetos.
# Es la forma recomendada para la mayoría de las operaciones.

def registrar_nuevos_profesionales_orm():
    """Registra 5 nuevos profesionales usando objetos de SQLAlchemy."""
    
    db = SessionLocal()

    # Datos de los primeros 5 profesionales
    nuevos_profesionales = [
        Profesional(id=11, nombre='Dr/a. Sofía Castro', especialidad='Pediatría', horario='Lun a Vie 9-17'),
        Profesional(id=12, nombre='Dr/a. Mateo Vargas', especialidad='Traumatología', horario='Lun a Vie 9-17'),
        Profesional(id=13, nombre='Dr/a. Valentina Herrera', especialidad='Ginecología', horario='Lun a Vie 8-16'),
        Profesional(id=14, nombre='Dr/a. Lucas Muñoz', especialidad='Oftalmología', horario='Lun a Vie 10-18'),
        Profesional(id=15, nombre='Dr/a. Isabella Rojas', especialidad='Pediatría', horario='Lun a Vie 8-16')
    ]

    try:
        print("--- Iniciando registro con SQLAlchemy ORM ---")
        db.add_all(nuevos_profesionales) # Agregamos la lista de objetos a la sesión
        db.commit() # Confirmamos la transacción
        print("¡5 profesionales registrados exitosamente con el método ORM!")

        for prof in nuevos_profesionales:
            db.refresh(prof) # Actualizamos los objetos para tener la info de la DB
            print(f"  -> ID: {prof.id}, Nombre: {prof.nombre}")

    except Exception as e:
        print(f"Error al registrar con ORM: {e}")
        db.rollback()
    finally:
        db.close()


# --- MÉTODO 2: Usando SQL Nativo (Directo) ---
# Ventajas: Puede ser más rápido para operaciones masivas complejas. Útil si ya tienes
# un script SQL que quieres ejecutar.
# Desventajas: ¡PELIGRO DE INYECCIÓN SQL SI NO SE USA CORRECTAMENTE!

def registrar_nuevos_profesionales_sql():
    """Registra 5 nuevos profesionales usando sentencias SQL directas."""

    db = SessionLocal()

    # Datos de los siguientes 5 profesionales
    otros_profesionales = [
        {'id': 16, 'nombre': 'Dr/a. Martín Flores', 'especialidad': 'Cardiología', 'horario': 'Mar y Jue 8-15'},
        {'id': 17, 'nombre': 'Dr/a. Camila Castillo', 'especialidad': 'Dermatología', 'horario': 'Lun, Mie, Vie 9-15'},
        {'id': 18, 'nombre': 'Dr/a. Benjamín Soto', 'especialidad': 'Traumatología', 'horario': 'Mar y Jue 10-18'},
        {'id': 19, 'nombre': 'Dr/a. Emilia Morales', 'especialidad': 'Clínica médica', 'horario': 'Lun a Vie 8-16'},
        {'id': 20, 'nombre': 'Dr/a. Daniel Paredes', 'especialidad': 'Oftalmología', 'horario': 'Mie a Vie 10-18'}
    ]

    try:
        print("\n--- Iniciando registro con SQL Directo ---")
        for prof in otros_profesionales:
            # IMPORTANTE: Usamos text() y parámetros (:nombre, :especialidad, etc.)
            # para que SQLAlchemy sanitice los datos y prevenga inyección SQL.
            # ¡Nunca uses f-strings para construir una consulta con datos externos!
            query = text("""
                INSERT INTO profesionales (id, nombre, especialidad, horario)
                VALUES (:id, :nombre, :especialidad, :horario)
            """)
            db.execute(query, prof) # Pasamos el diccionario como parámetro
        
        db.commit() # Confirmamos la transacción
        print("¡5 profesionales registrados exitosamente con el método SQL Directo!")
        for prof in otros_profesionales:
            print(f"  -> ID: {prof['id']}, Nombre: {prof['nombre']}")

    except Exception as e:
        print(f"Error al registrar con SQL Directo: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    registrar_nuevos_profesionales_orm()
    registrar_nuevos_profesionales_sql()