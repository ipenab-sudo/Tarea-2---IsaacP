# Problema 3: Precio final de un producto con impuesto
 
# ----- Entrada -----
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
 
# ----- Proceso -----
tasa_impuesto = 0.13    # constante: 13 % de impuesto
monto_impuesto = precio_producto * tasa_impuesto
precio_final = precio_producto + monto_impuesto
 
# ----- Salida -----
print("Producto:", nombre_producto)
print("Impuesto (13%): ₡" + format(monto_impuesto, ",.2f"))
print("Precio final: ₡" + format(precio_final, ",.2f"))
