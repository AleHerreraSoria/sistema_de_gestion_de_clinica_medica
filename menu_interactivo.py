# menu_interactivo.py

from database import SessionLocal
from sqlalchemy import text
import datetime

def llamar_sp_registrar_profesional():
    """Pide datos por consola y llama al SP para registrar un profesional."""
    print("\n--- Registrar Nuevo Profesional ---")
    try:
        p_id = int(input("Ingrese el ID del nuevo profesional: "))
        p_nombre = input("Ingrese el nombre completo: ")
        p_especialidad = input("Ingrese la especialidad: ")
        p_horario = input("Ingrese el horario: ")
        
        db = SessionLocal()
        # Los procedimientos se llaman con CALL
        query = text("CALL sp_registrar_profesional(:id, :nombre, :especialidad, :horario)")
        db.execute(query, {'id': p_id, 'nombre': p_nombre, 'especialidad': p_especialidad, 'horario': p_horario})
        db.commit()
        print("\n¡Profesional registrado exitosamente!")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        if 'db' in locals():
            db.close()

def llamar_sp_reprogramar_turnos():
    """Pide datos por consola y llama a la función para reprogramar turnos."""
    print("\n--- Reprogramar Turnos por Fecha ---")
    try:
        p_fecha = input("Ingrese la fecha a reprogramar (formato YYYY-MM-DD): ")
        # Validar formato de fecha
        datetime.datetime.strptime(p_fecha, '%Y-%m-%d')
        
        p_dias = int(input("Ingrese el número de días a desplazar (ej: 1 para el día siguiente): "))
        
        db = SessionLocal()
        # Las funciones que devuelven valor se llaman con SELECT
        query = text("SELECT sp_reprogramar_turnos_por_fecha(:fecha, :dias)")
        resultado = db.execute(query, {'fecha': p_fecha, 'dias': p_dias}).scalar()
        db.commit()
        print(f"\n¡Operación completada! Se reprogramaron {resultado} turnos.")
    except ValueError:
        print("\nError: Formato de fecha o número de días inválido.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        if 'db' in locals():
            db.close()

def llamar_sp_cancelar_todos_futuros():
    """Llama a la función para cancelar todos los turnos futuros."""
    print("\n--- Cancelar TODOS los Turnos Futuros ---")
    confirmacion = input("¿Está seguro de que desea cancelar TODOS los turnos futuros? Esta acción es irreversible. (s/n): ")
    if confirmacion.lower() != 's':
        print("Operación cancelada.")
        return
        
    try:
        db = SessionLocal()
        query = text("SELECT sp_cancelar_todos_los_turnos_futuros()")
        resultado = db.execute(query).scalar()
        db.commit()
        print(f"\n¡Operación completada! Se cancelaron {resultado} turnos futuros.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        if 'db' in locals():
            db.close()

def llamar_sp_cancelar_paciente():
    """Pide un nombre y llama a la función para cancelar los turnos futuros de ese paciente."""
    print("\n--- Cancelar Turnos Futuros de un Paciente ---")
    try:
        p_nombre = input("Ingrese el nombre completo del paciente: ")
        
        db = SessionLocal()
        query = text("SELECT sp_cancelar_turnos_futuros_paciente(:nombre)")
        resultado = db.execute(query, {'nombre': p_nombre}).scalar()
        db.commit()
        
        if resultado == -1:
            print(f"\nNo se encontró al paciente '{p_nombre}'. No se canceló ningún turno.")
        else:
            print(f"\n¡Operación completada! Se cancelaron {resultado} turnos para el paciente '{p_nombre}'.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        if 'db' in locals():
            db.close()

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n===== MENÚ DE GESTIÓN DEL CENTRO MÉDICO =====")
    print("1. Registrar Nuevo Profesional")
    print("2. Reprogramar Turnos por Fecha")
    print("3. Cancelar TODOS los Turnos Futuros")
    print("4. Cancelar Turnos Futuros de un Paciente")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    """Función principal que ejecuta el menú interactivo."""
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            llamar_sp_registrar_profesional()
        elif opcion == '2':
            llamar_sp_reprogramar_turnos()
        elif opcion == '3':
            llamar_sp_cancelar_todos_futuros()
        elif opcion == '4':
            llamar_sp_cancelar_paciente()
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()