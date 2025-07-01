# cancelar_turnos.py

import datetime
from database import SessionLocal
from models import Turno, Paciente
from sqlalchemy import and_

# --- Función 1: Cancelar TODOS los turnos futuros ---

def cancelar_todos_los_turnos_futuros():
    """
    Busca y elimina todos los turnos cuya fecha sea igual o posterior a hoy.
    """
    db = SessionLocal()
    hoy = datetime.date.today()
    
    print(f"--- 1. INICIANDO CANCELACIÓN DE TODOS LOS TURNOS FUTUROS (a partir del {hoy}) ---")
    
    try:
        # Buscamos los turnos para saber cuántos se van a borrar
        turnos_a_borrar = db.query(Turno).filter(Turno.fecha >= hoy).all()
        
        if not turnos_a_borrar:
            print("No se encontraron turnos futuros para cancelar.")
            return

        print(f"Se encontraron {len(turnos_a_borrar)} turnos futuros que serán cancelados.")

        # Realizamos el borrado masivo. Es más eficiente que borrar uno por uno.
        # El 'synchronize_session=False' es una recomendación para borrados masivos.
        num_filas_borradas = db.query(Turno).filter(Turno.fecha >= hoy).delete(synchronize_session=False)

        db.commit() # Confirmamos la transacción para que el borrado sea permanente

        print(f"\n¡ÉXITO! Se han cancelado {num_filas_borradas} turnos futuros.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        db.rollback()
    finally:
        db.close()


# --- Función 2: Cancelar turnos futuros de un PACIENTE ESPECÍFICO ---

def cancelar_turnos_futuros_paciente(nombre_completo_paciente: str):
    """
    Busca y elimina los turnos futuros para un paciente identificado por su nombre.
    
    Args:
        nombre_completo_paciente (str): El nombre y apellido exacto del paciente.
    """
    db = SessionLocal()
    hoy = datetime.date.today()

    print(f"\n--- 2. INICIANDO CANCELACIÓN DE TURNOS FUTUROS PARA EL PACIENTE: '{nombre_completo_paciente}' ---")

    try:
        # Paso A: Encontrar el ID del paciente a partir de su nombre
        paciente = db.query(Paciente).filter(Paciente.nombre == nombre_completo_paciente).first()

        if not paciente:
            print(f"Error: No se encontró ningún paciente con el nombre '{nombre_completo_paciente}'.")
            return
        
        id_paciente = paciente.id
        print(f"Paciente encontrado (ID: {id_paciente}). Buscando sus turnos futuros...")

        # Paso B: Buscar los turnos para saber cuántos se borrarán
        turnos_a_borrar = db.query(Turno).filter(
            and_(
                Turno.paciente_id == id_paciente,
                Turno.fecha >= hoy
            )
        ).all()
        
        if not turnos_a_borrar:
            print(f"El paciente no tiene turnos futuros agendados.")
            return

        print(f"Se encontraron {len(turnos_a_borrar)} turnos futuros para este paciente.")

        # Paso C: Realizar el borrado masivo y condicional
        num_filas_borradas = db.query(Turno).filter(
            and_(
                Turno.paciente_id == id_paciente,
                Turno.fecha >= hoy
            )
        ).delete(synchronize_session=False)

        db.commit()

        print(f"\n¡ÉXITO! Se han cancelado {num_filas_borradas} turnos para {nombre_completo_paciente}.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    # --- EJECUCIÓN ---
    # Para probar las funciones, puedes descomentar la que quieras usar.
    # Es mejor ejecutarlas de una en una para poder verificar el resultado en DBeaver.
    
    # --- Prueba de la Función 1 ---
    # Descomenta la siguiente línea para borrar TODOS los turnos futuros.
    # ¡CUIDADO! Esta acción es irreversible.
    cancelar_todos_los_turnos_futuros()
    
    # --- Prueba de la Función 2 ---
    # Descomenta la siguiente línea para borrar los turnos de un paciente específico.
    # Vamos a usar 'Carlos Martínez' como ejemplo.
    # cancelar_turnos_futuros_paciente("Carlos Martínez")