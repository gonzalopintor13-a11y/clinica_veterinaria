import uuid
from src.models.veterinario import Veterinario

class GestionVeterinarios:
    def __init__(self):
        self.veterinarios = {}

    def _nuevo_id(self):
        return str(uuid.uuid4())[:8]

    def agregar_veterinario(self, nombre, especialidad):
        nuevo = Veterinario(self._nuevo_id(), nombre, especialidad)
        self.veterinarios[nuevo.id] = nuevo
        return nuevo

    def listar_veterinarios(self):
        return list(self.veterinarios.values())
