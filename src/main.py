from services.gestion_clientes import GestionClientes
from services.gestion_mascotas import GestionMascotas
from services.gestion_veterinarios import GestionVeterinarios
from services.gestion_citas import GestionCitas
from services.gestion_historias import GestionHistorias


def crear_sistema():
    gestion_clientes = GestionClientes()
    gestion_veterinarios = GestionVeterinarios()
    gestion_mascotas = GestionMascotas(gestion_clientes)
    gestion_citas = GestionCitas(gestion_mascotas, gestion_veterinarios)
    gestion_historias = GestionHistorias(gestion_mascotas)

    return {
        "clientes": gestion_clientes,
        "veterinarios": gestion_veterinarios,
        "mascotas": gestion_mascotas,
        "citas": gestion_citas,
        "historias": gestion_historias,
    }


if __name__ == "__main__":
    sistema = crear_sistema()
    print("Sistema cargado correctamente.")
