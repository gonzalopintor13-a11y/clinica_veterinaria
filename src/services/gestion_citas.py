import uuid
from datetime import datetime
from src.models.cita import Cita

class GestionCitas:
    def __init__(self, gestion_mascotas, gestion_veterinarios):
        self.citas = {}
        self.gestion_mascotas = gestion_mascotas
        self.gestion_veterinarios = gestion_veterinarios

    def _nuevo_id(self):
        return str(uuid.uuid4())[:8]

    def programar_cita(self, mascota_id, veterinario_id, fecha_hora: datetime, motivo):
        if not self.gestion_mascotas.mascotas.get(mascota_id):
            raise ValueError("Mascota no encontrada")
        if not self.gestion_veterinarios.veterinarios.get(veterinario_id):
            raise ValueError("Veterinario no encontrado")

        nueva = Cita(self._nuevo_id(), mascota_id, veterinario_id, fecha_hora, motivo)
        self.citas[nueva.id] = nueva
        return nueva

    def listar_citas(self):
        return list(self.citas.values())
