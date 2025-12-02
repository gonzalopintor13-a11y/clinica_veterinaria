"""
Script: veterinario.py
Descripción:
    Define la clase Veterinario, profesional encargado de atender mascotas.
    Se validan especialidad y número de colegiado.
"""

from dataclasses import dataclass

@dataclass
class Veterinario:
    id: int | None
    nombre: str
    especialidad: str      # cirugía, dermatología, etc.
    colegiado: str         # número de colegiado obligatorio

    def __post_init__(self):
        """Validación del número de colegiado."""

        if not self.colegiado.strip():
            raise ValueError("Número de colegiado inválido.")


