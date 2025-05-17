'''
Se pide obtener que tipo de triángulo es.
Sabiendo que ingresan 3 datos correspondientes al largo de cada lado.
Recordar: el triángulo equilátero tiene los 3 lados iguales, el isósceles 2 lados iguales y el escaleno los 3 lados distintos.
Versión con funciones: https://github.com/mnapo/ifts24-tecnicas-programacion-python2/blob/main/Ejercicio%2012.py
'''

lado1 = 0
lado2 = 0
lado3 = 0

while True:
  try:
    lado1=float(input("Ingrese la medida del lado:"))
    if lado1<=0:
      print("La medida del lado debe ser positiva, reingresar")
      continue
  except ValueError:
    print("La medida del lado es incorrecta, reingresar")
    continue
while True:
  try:
    lado2=float(input("Ingrese la medida del lado:"))
    if lado2<=0:
      print("La medida del lado debe ser positiva, reingresar")
      continue
  except ValueError:
    print("La medida del lado es incorrecta, reingresar")
    continue
while True:
  try:
    lado3=float(input("Ingrese la medida del lado:"))
    if lado3<=0:
      print("La medida del lado debe ser positiva, reingresar")
      continue
  except ValueError:
    print("La medida del lado es incorrecta, reingresar")
    continue

if lado1==lado2 and lado2==lado3:
  print("El triángulo es equilátero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
  print("El triángulo es isóceles")
else:
  print("El triángulo es escaleno")
