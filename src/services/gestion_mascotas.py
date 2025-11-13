import uuid
from datetime import date
from src.models.mascota import Mascota

class GestionMascotas:
    def __init__(self, gestion_clientes):
        self.mascotas = {}
        self.gestion_clientes = gestion_clientes

    def _nuevo_id(self):
        return str(uuid.uuid4())[:8]

    def agregar_mascota(self, nombre, especie, raza, fecha_nacimiento: date, propietario_id):
        if not self.gestion_clientes.obtener_cliente(propietario_id):
            raise ValueError("Propietario no encontrado")
        nueva = Mascota(self._nuevo_id(), nombre, especie, raza, fecha_nacimiento, propietario_id)
        self.mascotas[nueva.id] = nueva
        return nueva

    def listar_mascotas(self):
        return list(self.mascotas.values())
