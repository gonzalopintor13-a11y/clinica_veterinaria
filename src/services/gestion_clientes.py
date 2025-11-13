import uuid
from src.models.cliente import Cliente

class GestionClientes:
    def __init__(self):
        self.clientes = {}

    def _nuevo_id(self):
        return str(uuid.uuid4())[:8]

    def agregar_cliente(self, nombre, telefono, email):
        nuevo = Cliente(self._nuevo_id(), nombre, telefono, email)
        self.clientes[nuevo.id] = nuevo
        return nuevo

    def obtener_cliente(self, id_cliente):
        return self.clientes.get(id_cliente)

    def listar_clientes(self):
        return list(self.clientes.values())
