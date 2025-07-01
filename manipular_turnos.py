# manipular_turnos.py

import datetime
from sqlalchemy import text
from database import SessionLocal
from models import Turno

def reprogramar_turnos_por_fecha(fecha_original_str, dias_a_mover):
    """
    Busca todos los turnos en una fecha específica y los mueve
    sumando una cantidad determinada de días.

    Args:
        fecha_original_str (str): La fecha a buscar en formato 'YYYY-MM-DD'.
        dias_a_mover (int): El número de días para reprogramar (puede ser positivo o negativo).
    """
    db = SessionLocal()
    
    try:
        # Convertimos la fecha de string a un objeto date de Python
        fecha_original = datetime.datetime.strptime(fecha_original_str, '%Y-%m-%d').date()
        
        # --- Paso 1: Buscar todos los turnos en la fecha original ---
        print(f"--- Buscando turnos para la fecha: {fecha_original_str} ---")
        
        # Usamos el ORM para hacer la consulta de forma segura y legible
        turnos_a_reprogramar = db.query(Turno).filter(Turno.fecha == fecha_original).all()

        if not turnos_a_reprogramar:
            print(f"No se encontraron turnos agendados para la fecha {fecha_original_str}.")
            return

        print(f"Se encontraron {len(turnos_a_reprogramar)} turnos para reprogramar.")

        # --- Paso 2: Reprogramar cada turno ---
        print("\n--- Reprogramando turnos... ---")
        
        # Calculamos la nueva fecha
        nueva_fecha = fecha_original + datetime.timedelta(days=dias_a_mover)
        
        for turno in turnos_a_reprogramar:
            id_paciente = turno.paciente_id
            id_profesional = turno.profesional_id
            fecha_anterior = turno.fecha
            
            # Actualizamos el campo 'fecha' del objeto turno
            turno.fecha = nueva_fecha
            
            print(f"  -> Turno ID {turno.id} (Paciente: {id_paciente}, Profesional: {id_profesional}) "
                  f"movido del {fecha_anterior} al {turno.fecha}")

        # --- Paso 3: Confirmar todos los cambios en la base de datos ---
        db.commit()
        print("\n¡Reprogramación completada y guardada en la base de datos!")

    except Exception as e:
        print(f"Ha ocurrido un error durante la reprogramación: {e}")
        db.rollback() # Si algo falla, revertimos todos los cambios
    finally:
        db.close() # Siempre cerramos la conexión


if __name__ == "__main__":
    # Definimos la fecha a cancelar y a cuántos días mover los turnos
    FECHA_A_CANCELAR = "2025-05-31"
    DIAS_DE_REPROGRAMACION = 1 # Moverlos al día siguiente

    reprogramar_turnos_por_fecha(FECHA_A_CANCELAR, DIAS_DE_REPROGRAMACION)