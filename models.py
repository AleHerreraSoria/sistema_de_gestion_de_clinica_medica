# models.py (Versión Final y Corregida)
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# ... (Actualizamos la clase 'Pacientes', tras agregar una nueva columna en DBeaver. las otras importaciones y clases no cambian) ...

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False, index=True)
    telefono = Column(String)
    
    # --- NUEVA LÍNEA AÑADIDA ---
    obra_social = Column(String(100)) # Usamos String(100) para que coincida con VARCHAR(100)
    # La relación no cambia

    turnos = relationship("Turno", back_populates="paciente")

# ... (las clases Profesional y Turno se mantienen igual) ...

class Profesional(Base):
    __tablename__ = 'profesionales'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    horario = Column(String)
    turnos = relationship("Turno", back_populates="profesional")

class Turno(Base):
    __tablename__ = 'turnos'
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    profesional_id = Column(Integer, ForeignKey('profesionales.id'), nullable=False)
    fecha = Column(Date, nullable=False)
    paciente = relationship("Paciente", back_populates="turnos")
    profesional = relationship("Profesional", back_populates="turnos")