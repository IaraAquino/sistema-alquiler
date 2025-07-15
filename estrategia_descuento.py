from abc import ABC, abstractmethod
from datetime import datetime

class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar_descuento(self, vehiculo, precio_original):
        pass

class SinDescuento(EstrategiaDescuento):
    def aplicar_descuento(self, vehiculo, precio_original):
        return precio_original

class DescuentoFinDeSemanaCombi(EstrategiaDescuento):
    def aplicar_descuento(self, vehiculo, precio_original):
        dia = datetime.today().weekday()
        if str(vehiculo) == "Combi" and dia in [5, 6]:  # 5 = sábado o 6 = domingo
            return precio_original * 0.85
        return precio_original
    
class DescuentoMartesCamion(EstrategiaDescuento):
    def aplicar_descuento(self, vehiculo, precio_original):
        dia = datetime.today().weekday()  # 1 = martes
        if str(vehiculo) == "Camión" and dia == 1:
            return precio_original * 0.80  # 20% de descuento
        return precio_original
