from dataclasses import dataclass
from datetime import datetime

@dataclass
class HistoriaClinica:
    id: str
    mascota_id: str
    fecha: datetime
    diagnostico: str
    tratamiento: str
    observaciones: str
