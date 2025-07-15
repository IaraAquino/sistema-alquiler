from vehiculos import Auto, Combi, CamionetaCarga, Camion
from gestor_vehiculos import GestorVehiculos
from cliente import Cliente
from estrategia_descuento import DescuentoFinDeSemanaCombi
from estrategia_descuento import DescuentoMartesCamion


gestor = GestorVehiculos()
# Lista de clientes con sus respectivos vehículos
clientes = [
    Cliente("Lucía", Auto("AAA111", 4)),
    Cliente("Ramiro", Auto("AAA222", 3)),
    Cliente("Sofía", Auto("AAA333", 2)),
    Cliente("Pablo", Combi("COM111", 6), DescuentoFinDeSemanaCombi()),
    Cliente("Ana", Combi("COM222", 8), DescuentoFinDeSemanaCombi()),
    Cliente("Tomás", Combi("COM333", 9), DescuentoFinDeSemanaCombi()),
    Cliente("Luis", CamionetaCarga("CCA111", 1.5)),
    Cliente("Carla", CamionetaCarga("CCA222", 2.5)),
    Cliente("Diego", CamionetaCarga("CCA333", 3)),
    Cliente("María", Camion("CAM123", 10), DescuentoMartesCamion())
]

# Registrar los vehículos en el gestor
for cliente in clientes:
    gestor.agregar_vehiculo(cliente.vehiculo)

# Duraciones de alquiler a simular
duraciones = [1, 3, 5, 7]

# Simulación para cada duración
for dias in duraciones:
    print("\n" + "=" * 55)
    print(f"     RESUMEN DE ALQUILERES POR {dias} DÍA{'S' if dias > 1 else ''}")
    print("=" * 55)
    print(f"{'Cliente':<15} {'Tipo de Vehículo':<25} {'Patente':<10} {'Costo (ARS)':>10}")
    print("-" * 55)
    for cliente in clientes:
        cliente.mostrar_resumen(dias)

print("\nGracias por utilizar nuestro sistema de alquiler de vehículos. ¡Hasta la próxima!")

# Mostrar los vehículos registrados en el gestor
print("\nVehículos registrados:")
for v in gestor.obtener_vehiculos():
    print(f"- {str(v):<25} {v.get_patente()}")
