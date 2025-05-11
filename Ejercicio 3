"""
Crear un programa que pida números enteros positivos indefinidamente.
El programa termina cuando se introduce un número negativo.
Finalmente, el programa muestra la suma de todos los números introducidos.
"""

total = 0
numero_ingresado = 0
print("A continuación, ingrese números enteros. Serán sumados hasta que ingrese uno negativo, y se mostrará el total")
while numero_ingresado>=0:
  total+=numero_ingresado
  try:
    numero_ingresado = int(input("Ingrese un entero:"))
  except ValueError:
    print("El valor ingresado no es un entero")
    numero_ingresado = 0
print("El total es", total)
