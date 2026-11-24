# Problema 5: Convertir minutos a horas y minutos
 
# ----- Entrada -----
minutos_totales = int(input("Ingrese la cantidad de minutos: "))
 
# ----- Proceso -----
minutos_por_hora = 60    # constante
horas = minutos_totales // minutos_por_hora
minutos_restantes = minutos_totales % minutos_por_hora
 
# ----- Salida -----
print(minutos_totales, "minutos equivalen a", horas, "horas y", minutos_restantes, "minutos")
