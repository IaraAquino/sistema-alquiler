from vehiculos.Vehiculo import Vehiculo
from vehiculos.Auto import Auto
class Combi(Auto):
    def __init__(self, patente: str, plazas: int):
        super().__init__(patente, plazas)

    def calcular_precio_alquiler(self, dias: int) -> float:
        return super().calcular_precio_alquiler(dias) + (Vehiculo.precio_base * 0.02 * self._plazas)

    def __str__(self) -> str:
        return "Combi"
