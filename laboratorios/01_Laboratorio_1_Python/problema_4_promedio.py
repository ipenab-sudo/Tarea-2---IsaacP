# Problema 4: Promedio de tres notas
 
# ----- Entrada -----
nombre_estudiante = input("Nombre del estudiante: ")
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))
 
# ----- Proceso -----
cantidad_notas = 3    # constante
suma_notas = nota_1 + nota_2 + nota_3
promedio = suma_notas / cantidad_notas
 
# ----- Salida -----
print("Promedio sin formato:", promedio)
print("Promedio con round:", round(promedio, 2))
print("El promedio de " + nombre_estudiante + " es " + format(promedio, ".2f"))
