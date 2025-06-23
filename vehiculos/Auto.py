from vehiculos.Vehiculo import Vehiculo
class Auto(Vehiculo):
    def __init__(self, patente: str, plazas: int):
        super().__init__(patente)
        self._plazas = plazas

    def calcular_precio_alquiler(self, dias: int) -> float:
        return dias * (Vehiculo.precio_base + (Vehiculo.precio_base * 0.015 * self._plazas))

    def __str__(self) -> str:
        return "Auto"
