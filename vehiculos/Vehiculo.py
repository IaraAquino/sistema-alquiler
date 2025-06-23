from abc import ABC, abstractmethod

class Vehiculo(ABC):
    precio_base = 500.0

    def __init__(self, patente: str):
        # Assuming patente is not None and not empty as per Java comment
        self._patente = patente

    @abstractmethod
    def calcular_precio_alquiler(self, dias: int) -> float:
        pass

    def get_patente(self) -> str:
        return self._patente

    @staticmethod
    def set_precio_base(precio_nuevo: float):
        Vehiculo.precio_base = precio_nuevo

    @abstractmethod
    def __str__(self) -> str:
        pass
