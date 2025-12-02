"""
Script: historias.py
Descripción:
    Contiene la clase HistoriaClinica, que almacena entradas médicas
    sobre una mascota. Se incluye validación básica y fecha automática.
"""

from dataclasses import dataclass
from datetime import date

@dataclass
class HistoriaClinica:
    id: int | None
    id_mascota: int
    descripcion: str
    fecha: date = date.today()

    def __post_init__(self):
        """Validación de la historia clínica."""

        if not self.descripcion.strip():
            raise ValueError("La descripción de la historia clínica no puede estar vacía.")


