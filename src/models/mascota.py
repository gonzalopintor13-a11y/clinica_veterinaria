"""
Script: mascota.py
Descripción:
    Define la clase Mascota, que representa a un animal atendido en la clínica veterinaria.
    Incluye atributos básicos y validaciones iniciales para asegurar la coherencia de los datos.
"""

from dataclasses import dataclass
from datetime import date

@dataclass
class Mascota:
    id: int | None
    nombre: str
    especie: str          # perro, gato, hurón...
    raza: str
    edad: int
    id_cliente: int       # dueño de la mascota
    fecha_registro: date = date.today()

    def __post_init__(self):
        """Validaciones automáticas después de crear la instancia."""
        
        # La edad no puede ser negativa
        if self.edad < 0:
            raise ValueError("La edad de la mascota no puede ser negativa.")

        # El nombre no debe estar vacío
        if not self.nombre.strip():
            raise ValueError("El nombre de la mascota no puede estar vacío.")


