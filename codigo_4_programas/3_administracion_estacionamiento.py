# Archivo: 3_administracion_estacionamiento.py
# Curso: Principios de Programacion 1
# Autor: Isaac Peña Brenes
# Fecha: 23/11/2026
# Version: 1.3
# Descripcion: Administra ingresos, salidas, ocupacion y recaudacion de un estacionamiento.

# Constantes del estacionamiento.
CAPACIDAD_MAXIMA = 20
TARIFA_POR_HORA = 800

# Inicializacion de los datos
vehiculos_presentes = 0
salidas_registradas = 0
recaudacion_total = 0

print("--- ADMINISTRACION DEL ESTACIONAMIENTO ---")

# Menu repetitivo: solo termina cuando se selecciona la opcion 5.
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupacion")
    print("4. Consultar recaudacion")
    print("5. Salir")

    opcion = input("Seleccione una opcion (1-5): ")

    # Seleccion de la operacion solicitada con match-case.
    match opcion:
        case "1":
            if vehiculos_presentes < CAPACIDAD_MAXIMA:
                vehiculos_presentes += 1
                print("Ingreso registrado correctamente.")
                print(f"Vehiculos presentes: {vehiculos_presentes}")
            else:
                print("No se puede registrar el ingreso: el estacionamiento esta lleno.")

        case "2":
            if vehiculos_presentes == 0:
                print("No se puede registrar una salida: el estacionamiento esta vacio.")
            else:
                # Validacion: se aceptan solo horas enteras mayores que cero.
                horas_cobradas = int(input("Horas enteras por cobrar: "))
                while horas_cobradas <= 0:
                    print("Error: ingrese un numero entero de horas mayor que cero.")
                    horas_cobradas = int(input("Horas enteras por cobrar: "))

                # Proceso de cobro y actualizacion de los registros.
                pago_salida = horas_cobradas * TARIFA_POR_HORA
                vehiculos_presentes -= 1
                salidas_registradas += 1
                recaudacion_total += pago_salida

                print(f"Pago registrado: ₡{pago_salida:,}")
                print(f"Vehiculos presentes: {vehiculos_presentes}")

        case "3":
            espacios_libres = CAPACIDAD_MAXIMA - vehiculos_presentes
            print(f"Espacios ocupados: {vehiculos_presentes}")
            print(f"Espacios libres: {espacios_libres}")

        case "4":
            print(f"Recaudacion total: ₡{recaudacion_total:,}")
            print(f"Vehiculos que han salido: {salidas_registradas}")

        case "5":
            # Resumen final antes de terminar el programa.
            espacios_libres = CAPACIDAD_MAXIMA - vehiculos_presentes
            print("\n=== RESUMEN FINAL ===")
            print(f"Vehiculos presentes: {vehiculos_presentes}")
            print(f"Espacios libres: {espacios_libres}")
            print(f"Salidas registradas: {salidas_registradas}")
            print(f"Recaudacion total: ₡{recaudacion_total:,}")
            print("Programa finalizado.")
            break

        case _:
            print("Opcion no valida. Seleccione una opcion del 1 al 5.")
