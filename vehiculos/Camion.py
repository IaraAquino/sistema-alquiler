from vehiculos.Vehiculo import Vehiculo
from vehiculos.CamionetaCarga import CamionetaCarga
class Camion(CamionetaCarga):
    def __init__(self, patente: str, PMA: float):
        super().__init__(patente, PMA)

    def calcular_precio_alquiler(self, dias: int) -> float:
        return super().calcular_precio_alquiler(dias) + (Vehiculo.precio_base * 0.4)

    def __str__(self) -> str:
        return "Camión"
