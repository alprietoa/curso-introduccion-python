def mayor(numeros):
    mayor_encontrado = numeros[0]

    for numero in numeros:
        if numero > mayor_encontrado:
            mayor_encontrado = numero

    return mayor_encontrado

def media(numeros):
    suma = 0

    for numero in numeros:
        suma += numero

    return suma / len(numeros)

lista = [4, 8, 2, 10, 3]

print(mayor(lista))   # 10
print(media([4, 8, 2, 10, 6]))   # 6.0