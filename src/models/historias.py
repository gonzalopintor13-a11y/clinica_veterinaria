"""
Script: historias.py
Descripción:
    Modelo de datos para las entradas de historia clínica de una mascota.
    Cada entrada registra la intervención de un veterinario, el motivo de la consulta,
    diagnóstico, tratamiento y fecha del registro.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class HistoriaClinica:
    id: int | None
    mascota_id: int
    vet_id: int | None
    motivo: str
    diagnostico: str
    tratamiento: str
    fecha: datetime = datetime.now()

    def __post_init__(self):
        """Validación básica de la entrada de historia clínica."""

        if not self.motivo.strip():
            raise ValueError("El motivo de la consulta no puede estar vacío.")

        if not self.diagnostico.strip():
            raise ValueError("El diagnóstico no puede estar vacío.")

        if not self.tratamiento.strip():
            raise ValueError("El tratamiento no puede estar vacío.")



