"""Excepciones personalizadas del sistema Software FJ."""

class SoftwareFJError(Exception):
    """Excepción base para errores controlados de la aplicación."""

class DatosInvalidosError(SoftwareFJError):
    """Se presenta cuando un dato no cumple las validaciones."""

class ServicioNoDisponibleError(SoftwareFJError):
    """Se presenta cuando un servicio no está disponible."""

class ReservaError(SoftwareFJError):
    """Se presenta cuando una reserva no puede crearse o procesarse."""

class EstadoReservaError(ReservaError):
    """Se presenta cuando una operación no corresponde al estado actual."""
