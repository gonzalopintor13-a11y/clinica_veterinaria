from dataclasses import dataclass
from datetime import date

@dataclass
class Mascota:
    id: str
    nombre: str
    especie: str
    raza: str
    fecha_nacimiento: date
    propietario_id: str  # Relación con Cliente
