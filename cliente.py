from estrategia_descuento import SinDescuento

class Cliente:
    
    def __init__(self, nombre, vehiculo, estrategia=None):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.estrategia = estrategia if estrategia else SinDescuento()

    def mostrar_resumen(self, dias):
        precio_base = self.vehiculo.calcular_precio_alquiler(dias)
        precio_final = self.estrategia.aplicar_descuento(self.vehiculo, precio_base)

        tipo = str(self.vehiculo)
        patente = self.vehiculo.get_patente()
        print(f"{self.nombre:<15} {tipo:<25} {patente:<10} ${precio_final:>10.2f}")
