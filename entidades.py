"""Entidades generales del sistema usando abstracción y encapsulación."""
from abc import ABC, abstractmethod
from datetime import datetime

class Entidad(ABC):
    """Clase abstracta que representa una entidad identificable."""
    def __init__(self, identificador):
        if not identificador or not str(identificador).strip():
            raise ValueError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()
        self._fecha_creacion = datetime.now()

    @property
    def identificador(self):
        return self._identificador

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @abstractmethod
    def describir(self):
        """Devuelve una descripción de la entidad."""
        raise NotImplementedError
