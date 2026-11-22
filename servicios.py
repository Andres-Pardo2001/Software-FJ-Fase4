"""Servicios especializados con herencia y polimorfismo."""
from abc import abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError, ServicioNoDisponibleError

class Servicio(Entidad):
    def __init__(self, identificador, nombre, tarifa_base, disponible=True):
        super().__init__(identificador)
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")
        if not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
            raise DatosInvalidosError("La tarifa base debe ser mayor que cero.")
        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)
        self.disponible = bool(disponible)

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no está disponible.")

    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        """Sobrecarga simulada mediante parámetros opcionales:
        costo básico, con impuesto y/o con descuento.
        """
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser un número mayor que cero.")
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self.tarifa_base * duracion
        return round(subtotal * (1 - descuento) * (1 + impuesto), 2)

    @abstractmethod
    def describir(self):
        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self, duracion):
        raise NotImplementedError

class ReservaSala(Servicio):
    def __init__(self, identificador, nombre, tarifa_base, capacidad, disponible=True):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        if not isinstance(capacidad, int) or capacidad < 1:
            raise DatosInvalidosError("La capacidad de la sala debe ser un entero positivo.")
        self.capacidad = capacidad

    def validar_parametros(self, duracion):
        self.validar_disponibilidad()
        if duracion > 12:
            raise DatosInvalidosError("La sala puede reservarse máximo 12 horas por operación.")

    def describir(self):
        return f"Sala: {self.nombre}. Capacidad: {self.capacidad} personas."

class AlquilerEquipo(Servicio):
    def __init__(self, identificador, nombre, tarifa_base, unidades, disponible=True):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        if not isinstance(unidades, int) or unidades < 1:
            raise DatosInvalidosError("Las unidades deben ser un entero positivo.")
        self.unidades = unidades

    def validar_parametros(self, duracion):
        self.validar_disponibilidad()
        if duracion > 168:
            raise DatosInvalidosError("El alquiler no puede superar 168 horas.")

    def describir(self):
        return f"Equipo: {self.nombre}. Unidades disponibles: {self.unidades}."

class AsesoriaEspecializada(Servicio):
    def __init__(self, identificador, nombre, tarifa_base, especialidad, disponible=True):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("La especialidad es obligatoria.")
        self.especialidad = especialidad.strip()

    def validar_parametros(self, duracion):
        self.validar_disponibilidad()
        if duracion > 8:
            raise DatosInvalidosError("La asesoría no puede superar 8 horas.")

    def describir(self):
        return f"Asesoría: {self.nombre}. Especialidad: {self.especialidad}."
