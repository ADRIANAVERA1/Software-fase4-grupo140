from abc import ABC, abstractmethod
from excepciones import ServicioError

# CLASE ABSTRACTA

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if not nombre or not nombre.strip():
            raise ServicioError("El nombre del servicio no puede estar vacío")

        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise ServicioError("La tarifa debe ser un número mayor a cero")

        self._nombre = nombre
        self._tarifa = tarifa

    def get_nombre(self):
        return self._nombre

    def get_tarifa(self):
        return self._tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

# SERVICIO 1: SALA

class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        return self._tarifa * horas


# SERVICIO 2: EQUIPOS

class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        return (self._tarifa * horas) + 2000  # cargo fijo


# SERVICIO 3: ASESORÍA

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        return (self._tarifa * horas) * 1.15  # impuesto 15%
