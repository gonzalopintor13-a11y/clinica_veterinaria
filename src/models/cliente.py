"""
Script: cliente.py
Descripción:
    Define la clase Cliente, que representa al dueño de una o varias mascotas.
    Incluye validaciones básicas (email, teléfono...) y fecha de registro automática.
"""

from dataclasses import dataclass
from datetime import date

@dataclass
class Cliente:
    id: int | None
    nombre: str
    telefono: str
    email: str
    fecha_registro: date = date.today()

    def __post_init__(self):
        """Validaciones automáticas del cliente."""

        # El email debe tener formato mínimo válido
        if "@" not in self.email:
            raise ValueError("Email inválido.")

        # Teléfono mínimo de 9 dígitos
        if len(self.telefono) < 9:
            raise ValueError("Teléfono inválido.")

