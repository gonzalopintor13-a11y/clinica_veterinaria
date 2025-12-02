"""
Tests para DataBaseConnector
Verifica inicialización, errores y conexión básica.
"""

import os
import pytest
from src.db.db_connector import DataBaseConnector


def test_db_connector_init_ok(tmp_path):
    """Debe inicializar el conector con un fichero válido."""
    
    fake_db = tmp_path / "test.db"
    fake_db.touch()  # crea archivo vacío

    conn = DataBaseConnector(str(fake_db))

    assert conn.db_path == str(fake_db)


def test_db_connector_init_fail():
    """Debe lanzar error si el archivo no existe."""

    with pytest.raises(FileNotFoundError):
        DataBaseConnector("no_existe.db")


def test_db_connector_connect_ok(tmp_path):
    """Debe conectar sin errores a SQLite."""

    fake_db = tmp_path / "test.db"
    fake_db.touch()

    conn = DataBaseConnector(str(fake_db))
    connection = conn.connect()

    assert connection is not None
    assert connection.cursor() is not None

