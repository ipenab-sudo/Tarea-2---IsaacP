nota = int(input("Ingresa tu nota (0-100): "))
 
match nota:
    case n if n < 0 or n > 100:
        print("Nota fuera de rango")
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Aprobado")
    case _:
        print("Reprobado")
