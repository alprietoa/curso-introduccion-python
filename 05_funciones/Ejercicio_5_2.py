def precio_final(precio, descuento):
    if descuento < 0 or descuento > 100:
        return "El descuento debe estar entre 0 y 100"

    cantidad_descuento = precio * descuento / 100
    return precio - cantidad_descuento


print(precio_final(100, 20))   # 80.0
print(precio_final(100, 120))  # El descuento debe estar entre 0 y 100