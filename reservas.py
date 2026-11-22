"""Creación, confirmación, cancelación y procesamiento de reservas."""
from enum import Enum
from entidades import Entidad
from excepciones import ReservaError, EstadoReservaError

class EstadoReserva(Enum):
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    PROCESADA = "Procesada"

class Reserva(Entidad):
    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)
        if cliente is None or servicio is None:
            raise ReservaError("La reserva requiere un cliente y un servicio.")
        servicio.validar_parametros(duracion)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = EstadoReserva.PENDIENTE
        self.costo = servicio.calcular_costo(duracion)

    def confirmar(self):
        if self.estado != EstadoReserva.PENDIENTE:
            raise EstadoReservaError("Solo se pueden confirmar reservas pendientes.")
        self.estado = EstadoReserva.CONFIRMADA
        return self.estado.value

    def cancelar(self):
        if self.estado not in (EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA):
            raise EstadoReservaError("La reserva no se puede cancelar en su estado actual.")
        self.estado = EstadoReserva.CANCELADA
        return self.estado.value

    def procesar(self):
        if self.estado != EstadoReserva.CONFIRMADA:
            raise EstadoReservaError("Solo se pueden procesar reservas confirmadas.")
        self.estado = EstadoReserva.PROCESADA
        return f"Reserva {self.identificador} procesada. Total: ${self.costo:,.2f}"

    def describir(self):
        return (f"Reserva {self.identificador} | Cliente: {self.cliente.nombre} | "
                f"Servicio: {self.servicio.nombre} | Estado: {self.estado.value} | "
                f"Costo: ${self.costo:,.2f}")
