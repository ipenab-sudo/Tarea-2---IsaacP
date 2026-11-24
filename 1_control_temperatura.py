# Archivo: 1_control_temperatura.py
# Curso: Principios de Programacion 1
# Autor: Isaac Peña Brenes
# Fecha: 23/11/2026
# Version: 1.2
# Descripcion: Simula el aumento progresivo de temperatura de una camara experimental.

print("=== CONTROL DE TEMPERATURA ===")

# Entrada: se ingresan directamente valores numericos.
temperatura_inicial = float(input("Temperatura inicial (°C): "))
temperatura_objetivo = float(input("Temperatura objetivo (°C): "))
incremento = float(input("Incremento por ciclo (°C): "))

# Decision: se comprueba que la configuracion permita iniciar el calentamiento.
if temperatura_objetivo <= temperatura_inicial:
    print("Error: la temperatura objetivo debe ser mayor que la inicial.")
elif incremento <= 0:
    print("Error: el incremento debe ser estrictamente positivo.")
else:
    # Inicializacion y proceso iterativo.
    temperatura_actual = temperatura_inicial
    ciclos = 0

    print("\nInicia la simulacion:")
    while temperatura_actual < temperatura_objetivo:
        temperatura_actual += incremento
        ciclos += 1
        print(f"Ciclo {ciclos}: {temperatura_actual} °C")

    # Salida: se presenta el resultado final.
    print("\n=== RESULTADO FINAL ===")
    print(f"Temperatura alcanzada: {temperatura_actual} °C")
    print(f"Total de ciclos: {ciclos}")
