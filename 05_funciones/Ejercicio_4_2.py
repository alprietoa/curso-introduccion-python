def clasificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"


print(clasificar_numero(7))    # positivo
print(clasificar_numero(-3))   # negativo
print(clasificar_numero(0))    # cero