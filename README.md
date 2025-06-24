# Sistema de Alquiler de Vehículos

## Problemática

Se desea desarrollar una aplicación que permita calcular los precios de alquiler de una empresa de 
alquiler de vehículos.  
Cada vehículo se identifica por medio de su patente.  
La empresa alquila distintos tipos de vehículos, tanto para transporte de personas como de carga. 
En la actualidad los vehículos alquilados por la empresa: autos, combis, camionetas de carga y 
camiones.  
El precio del alquiler de cualquier vehículo tiene una componente base de alquiler a razón de $500 
por día.  
En el caso de alquiler de un auto, al precio base diario se lo incrementa un 1.5 % por plaza. El 
precio de alquiler de las combis es igual al de los coches, salvo que se le añade un 2% por plaza 
independiente de la cantidad de días de alquiler.  
El precio de los vehículos de carga es el precio base diario incrementado un 20% * PMA (PMA 
=peso máximo autorizado en toneladas), de modo que si el vehículo tiene una capacidad descarga 
1.5 toneladas, al precio base diario se lo incrementará un 30%.  
En el caso de los camiones, al precio se le suma un fijo del 40% independientemente de la 
cantidad de días de alquiler.  

## Funcionalidades

Este es un sistema por consola que simula el alquiler de distintos tipos de vehículos: autos, combis, camionetas de carga y camiones. Cada vehículo tiene su propia lógica de precios, y el sistema calcula el costo total según la cantidad de días de alquiler.

El sistema permite: 
- Crear clientes con vehículos asignados.
- Simular alquileres para distintas duraciones (1, 3, 5 y 7 días).
- Calcular y mostrar los costos de alquiler por cliente.
- Mostrar por consola una salida formateada tipo tabla.

## Instrucciones de ejecución

1. Asegúrese de tener **Python 3.8 o superior** instalado.
2. Abra una terminal y ubíquese en la carpeta donde está el archivo "main.py".
3. Ejecute el siguiente comando:

```bash
python main.py
