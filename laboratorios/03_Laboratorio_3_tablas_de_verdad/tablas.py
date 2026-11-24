# ---------- Operadores relacionales ----------
a = 10
b = 5
print("--- OPERADORES RELACIONALES (a = 10, b = 5) ---")
print("a == b  ->", a == b)
print("a != b  ->", a != b)
print("a >  b  ->", a > b)
print("a <  b  ->", a < b)
print("a >= b  ->", a >= b)
print("a <= b  ->", a <= b)
print()
 
# ---------- Tabla de verdad AND ----------
print("--- TABLA DE VERDAD: AND ---")
print("A      B      | A and B")
print("True   True   |", True and True)
print("True   False  |", True and False)
print("False  True   |", False and True)
print("False  False  |", False and False)
print()
 
# ---------- Tabla de verdad OR ----------
print("--- TABLA DE VERDAD: OR ---")
print("A      B      | A or B")
print("True   True   |", True or True)
print("True   False  |", True or False)
print("False  True   |", False or True)
print("False  False  |", False or False)
print()
 
# ---------- Tabla de verdad NOT ----------
print("--- TABLA DE VERDAD: NOT ---")
print("A      | not A")
print("True   |", not True)
print("False  |", not False)
print()
 
# ---------- Relacionales + lógicos ----------
edad = 20
tiene_licencia = False
print("--- COMBINANDO OPERADORES (edad = 20, tiene_licencia = False) ---")
print("edad >= 18 and tiene_licencia      ->", edad >= 18 and tiene_licencia)
print("edad >= 18 or tiene_licencia       ->", edad >= 18 or tiene_licencia)
print("not tiene_licencia                 ->", not tiene_licencia)
print("edad >= 18 and not tiene_licencia  ->", edad >= 18 and not tiene_licencia)
