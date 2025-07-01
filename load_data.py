# load_data.py
import pandas as pd
from database import SessionLocal
from models import Paciente, Profesional, Turno
import os

DATA_DIR = "dataset_turnos"

def cargar_datos():
    db = SessionLocal()
    try:
        print("Iniciando la carga de datos...")

        pacientes_path = os.path.join(DATA_DIR, 'pacientes.csv')
        df_pacientes = pd.read_csv(pacientes_path)
        for _, row in df_pacientes.iterrows():
            db.merge(Paciente(id=row['id'], nombre=row['nombre'], dni=str(row['dni']), telefono=str(row['telefono'])))
        print(f" - {len(df_pacientes)} pacientes procesados.")

        profesionales_path = os.path.join(DATA_DIR, 'profesionales.csv')
        df_profesionales = pd.read_csv(profesionales_path)
        for _, row in df_profesionales.iterrows():
            db.merge(Profesional(id=row['id'], nombre=row['nombre'], especialidad=row['especialidad'], horario=row['horario']))
        print(f" - {len(df_profesionales)} profesionales procesados.")

        turnos_path = os.path.join(DATA_DIR, 'turnos.csv')
        df_turnos = pd.read_csv(turnos_path, parse_dates=['fecha'])
        for _, row in df_turnos.iterrows():
            db.merge(Turno(id=row['id'], paciente_id=row['paciente_id'], profesional_id=row['profesional_id'], fecha=row['fecha'].date()))
        print(f" - {len(df_turnos)} turnos procesados.")

        db.commit()
        print("\n¡Datos cargados y confirmados en la base de datos exitosamente!")
    except Exception as e:
        print(f"Ocurrió un error durante la carga de datos: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    cargar_datos()