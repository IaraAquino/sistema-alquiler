class Cliente:
    def __init__(self, nombre, vehiculo):
        self.nombre = nombre                      # Nombre del cliente
        self.vehiculo = vehiculo                  # Agregación: Cliente usa un Vehiculo

    def mostrar_resumen(self, dias):
        costo = self.vehiculo.calcular_precio_alquiler(dias)
        tipo = str(self.vehiculo)
        patente = self.vehiculo.get_patente()

        print(f"{self.nombre:<15} {tipo:<25} {patente:<10} ${costo:>10.2f}")
