# Archivo: 2_consumo_semanal_agua.py
# Curso: Principios de Programacion 1
# Autor: Isaac Peña Brenes
# Fecha: 23/11/2026
# Version: 1.2
# Descripcion: Registra siete consumos diarios y calcula el resumen semanal.

# Constantes del problema.
CANTIDAD_DIAS = 7
UMBRAL_CONSUMO = 150

# Inicializacion de contadores y acumuladores.
total_consumo = 0
consumo_maximo = 0
dias_superiores = 0

print("--- REGISTRO SEMANAL DE CONSUMO DE AGUA ---")

# Iteracion: la cantidad de jornadas esta definida desde el inicio.
for dia in range(1, CANTIDAD_DIAS + 1):
    consumo_diario = float(input(f"Consumo del dia {dia} (litros): "))

    # Validacion: no se permiten consumos negativos.
    while consumo_diario < 0:
        print("Error: el consumo no puede ser negativo. Intente de nuevo.")
        consumo_diario = float(input(f"Consumo del dia {dia} (litros): "))

    # Proceso: acumulacion, comparacion del maximo y conteo del umbral.
    total_consumo += consumo_diario

    if dia == 1 or consumo_diario > consumo_maximo:
        consumo_maximo = consumo_diario

    if consumo_diario > UMBRAL_CONSUMO:
        dias_superiores += 1

# Calculo y salida del resumen semanal.
promedio_diario = total_consumo / CANTIDAD_DIAS

print("\n=== RESUMEN SEMANAL ===")
print(f"Consumo total: {total_consumo} litros")
print(f"Promedio diario: {promedio_diario:.2f} litros")
print(f"Mayor consumo registrado: {consumo_maximo} litros")
print(f"Dias con consumo superior a {UMBRAL_CONSUMO} litros: {dias_superiores}")
