"""
Script: cita.py
Descripción:
    Define la clase Cita, que representa una visita programada entre
    un veterinario y una mascota. Incluye validación de fechas.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cita:
    id: int | None
    id_mascota: int
    id_veterinario: int
    fecha: datetime
    motivo: str

    def __post_init__(self):
        """Validaciones automáticas de la cita."""

        # La cita no puede ser creada en el pasado
        if self.fecha < datetime.now():
            raise ValueError("No se pueden crear citas en el pasado.")

        # El motivo no puede estar vacío
        if not self.motivo.strip():
            raise ValueError("El motivo de la cita no puede estar vacío.")


