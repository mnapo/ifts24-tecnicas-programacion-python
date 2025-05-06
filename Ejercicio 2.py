# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora.

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas:"))
costo_hora = float(input("Ingrese el costo por hora:"))
ingreso = horas_trabajadas * costo_hora
print("Ingreso: ", ingreso)
