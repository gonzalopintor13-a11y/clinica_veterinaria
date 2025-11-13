import uuid
from datetime import datetime
from src.models.historias import HistoriaClinica

class GestionHistorias:
    def __init__(self, gestion_mascotas):
        self.historias = {}
        self.gestion_mascotas = gestion_mascotas

    def _nuevo_id(self):
        return str(uuid.uuid4())[:8]

    def registrar_historia(self, mascota_id, diagnostico, tratamiento, observaciones):
        if mascota_id not in self.gestion_mascotas.mascotas:
            raise ValueError("Mascota no encontrada")
        nueva = HistoriaClinica(self._nuevo_id(), mascota_id, datetime.now(), diagnostico, tratamiento, observaciones)
        self.historias[nueva.id] = nueva
        return nueva

    def listar_historias(self):
        return list(self.historias.values())
