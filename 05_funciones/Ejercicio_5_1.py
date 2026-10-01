def precio_final(precio, descuento):
    cantidad_descuento = precio * descuento / 100
    resultado = precio - cantidad_descuento
    return resultado


print(precio_final(100, 20))   # 80.0
print(precio_final(50, 10))    # 45.0