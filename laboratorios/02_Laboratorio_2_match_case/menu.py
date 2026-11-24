# ---- Calculadora con menú (sin ciclos) ----
print("--- CALCULADORA ---")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
print("-------------------")
 
opcion = input("Elige una opción (1-5): ")
 
match opcion:
    case "1" | "2" | "3" | "4":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
 
        match opcion:
            case "1":
                print("Resultado:", a + b)
            case "2":
                print("Resultado:", a - b)
            case "3":
                print("Resultado:", a * b)
            case "4":
                if b == 0:
                    print("Error: no se puede dividir entre cero")
                else:
                    print("Resultado:", a / b)
    case "5":
        print("Saliendo del programa. ¡Hasta luego!")
    case _:
        print("Opción no válida")
