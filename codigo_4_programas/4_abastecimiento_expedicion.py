# Archivo: 4_abastecimiento_expedicion.py
# Curso: Principios de Programacion 1
# Autor: Isaac Peña Brenes
# Fecha: 23/11/2026
# Version: 1.1
# Descripcion: Simula el consumo de agua y alimento durante una expedicion.

# Existencias iniciales y limites de planificacion.
AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100
JORNADAS_MINIMAS = 1
JORNADAS_MAXIMAS = 30

# Inicializacion de los recursos y de los acumuladores.
agua_disponible = AGUA_INICIAL
alimento_disponible = ALIMENTO_INICIAL
agua_consumida_total = 0
alimento_consumido_total = 0
jornadas_completadas = 0
estado_expedicion = "Completada"

print("--- CONTROL DE ABASTECIMIENTO DE UNA EXPEDICION ---")

# Entrada validada: se aceptan de 1 a 30 jornadas enteras.
jornadas_planeadas = int(input("Cantidad de jornadas previstas (1-30): "))
while jornadas_planeadas < JORNADAS_MINIMAS or jornadas_planeadas > JORNADAS_MAXIMAS:
    print("Error: ingrese un numero entero entre 1 y 30.")
    jornadas_planeadas = int(input("Cantidad de jornadas previstas (1-30): "))

# Recorrido de los dias planificados.
for dia in range(1, jornadas_planeadas + 1):
    # Verificacion al inicio de cada jornada.
    if agua_disponible <= 0 or alimento_disponible <= 0:
        estado_expedicion = "Interrumpida por agotamiento de recursos"
        break

    print(f"\n--- JORNADA {dia} ---")

    # Validacion del consumo de agua: debe ser positivo y no superar el saldo.
    agua_consumida_dia = int(input(f"Agua consumida (litros, disponible {agua_disponible}): "))
    while agua_consumida_dia <= 0 or agua_consumida_dia > agua_disponible:
        print("Error: el consumo debe ser positivo y no superar el agua disponible.")
        agua_consumida_dia = int(input(f"Agua consumida (litros, disponible {agua_disponible}): "))

    # Validacion del consumo de alimento: debe ser positivo y no superar el saldo.
    alimento_consumido_dia = int(input(f"Alimento consumido (unidades, disponible {alimento_disponible}): "))
    while alimento_consumido_dia <= 0 or alimento_consumido_dia > alimento_disponible:
        print("Error: el consumo debe ser positivo y no superar el alimento disponible.")
        alimento_consumido_dia = int(input(f"Alimento consumido (unidades, disponible {alimento_disponible}): "))

    # Descuento de recursos y actualizacion de acumuladores.
    agua_disponible -= agua_consumida_dia
    alimento_disponible -= alimento_consumido_dia
    agua_consumida_total += agua_consumida_dia
    alimento_consumido_total += alimento_consumido_dia
    jornadas_completadas += 1

    print(f"Agua restante: {agua_disponible} litros")
    print(f"Alimento restante: {alimento_disponible} unidades")

    # Interrupcion anticipada si se agota un recurso y quedan jornadas pendientes.
    if (agua_disponible == 0 or alimento_disponible == 0) and dia < jornadas_planeadas:
        estado_expedicion = "Interrumpida por agotamiento de recursos"
        break

# Calculo de promedios con la cantidad real de jornadas completadas.
if jornadas_completadas > 0:
    promedio_agua_diario = agua_consumida_total / jornadas_completadas
    promedio_alimento_diario = alimento_consumido_total / jornadas_completadas
else:
    promedio_agua_diario = 0
    promedio_alimento_diario = 0

# Informe final.
print("\n--- INFORME FINAL DE LA EXPEDICION ---")
print(f"Jornadas planificadas: {jornadas_planeadas}")
print(f"Jornadas completadas: {jornadas_completadas}")
print(f"Agua consumida: {agua_consumida_total} litros")
print(f"Alimento consumido: {alimento_consumido_total} unidades")
print(f"Agua restante: {agua_disponible} litros")
print(f"Alimento restante: {alimento_disponible} unidades")
print(f"Promedio diario de agua: {promedio_agua_diario:.2f} litros")
print(f"Promedio diario de alimento: {promedio_alimento_diario:.2f} unidades")
print(f"Estado de la expedicion: {estado_expedicion}")
