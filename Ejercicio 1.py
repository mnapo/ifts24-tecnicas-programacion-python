# Calcular el promedio de nota obtenido por un alumno, teniendo 7 notas en el año.

suma_notas = 0
for i in range(6):
    print(i)
    nota = float(input("ingrese la nota:"))
    while (nota<0 or nota>10):
        nota = float(input("nota inválida, reingresar:"))
    suma_notas += nota
suma_notas = suma_notas / 7
print("El promedio es: ", suma_notas)