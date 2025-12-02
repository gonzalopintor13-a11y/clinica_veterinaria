"""
Tests para el modelo Mascota y su servicio.
Comprueba creación, validaciones y registro en el sistema.
"""

import pytest
from src.models.mascota import Mascota
from src.services.mascotas_service import MascotasService


def test_mascota_model_ok():
    """La mascota debe crearse correctamente."""

    m = Mascota(
        id=1,
        nombre="Rex",
        especie="Perro",
        edad=5,
        cliente_id=10
    )

    assert m.nombre == "Rex"
    assert m.especie == "Perro"
    assert m.edad == 5
    assert m.cliente_id == 10


def test_mascota_nombre_vacio():
    """Debe fallar si el nombre está vacío."""

    with pytest.raises(ValueError):
        Mascota(id=1, nombre="   ", especie="Perro", edad=3, cliente_id=10)


def test_mascotas_service_registro():
    """Debe agregar mascotas al servicio y listarlas."""

    svc = MascotasService()

    nueva = svc.registrar_mascota(
        nombre="Luna",
        especie="Gato",
        edad=2,
        cliente_id=99
    )

    assert nueva.id == 1  # primer ID automático
    assert len(svc.listar_mascotas()) == 1
    assert svc.listar_mascotas()[0].nombre == "Luna"
