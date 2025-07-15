class GestorVehiculos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._vehiculos = []
        return cls._instancia

    def agregar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self._vehiculos