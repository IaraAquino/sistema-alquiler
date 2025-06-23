from vehiculos.Vehiculo import Vehiculo
class CamionetaCarga(Vehiculo):
    def __init__(self, patente: str, PMA: float):
        super().__init__(patente)
        self._PMA = PMA

    def calcular_precio_alquiler(self, dias: int) -> float:
        return dias * (Vehiculo.precio_base + (Vehiculo.precio_base * 0.2 * self._PMA))

    def __str__(self) -> str:
        return "Camioneta de Carga"
