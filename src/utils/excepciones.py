class ClinicaError(Exception):
    """Error general de la clínica."""
    pass


class NoEncontradoError(ClinicaError):
    """Elemento no encontrado."""
    pass


class ValidacionError(ClinicaError):
    """Error de validación."""
    pass
