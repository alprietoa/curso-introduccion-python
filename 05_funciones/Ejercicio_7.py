def contar_consonantes(texto):
    contador = 0

    for letra in texto:
        if letra.lower() in "bcdfghjklmnñpqrstvwxyz":
            contador += 1

    return contador

def estadisticas_texto(texto):
    numero_caracteres = len(texto)
    numero_palabras = len(texto.split())
    numero_consonantes = contar_consonantes(texto)

    return numero_caracteres, numero_palabras, numero_consonantes


print(contar_consonantes("Hola mundo"))   # 5

caracteres, palabras, consonantes = estadisticas_texto("Hola mundo")
print("Caracteres:", caracteres)
print("Palabras:", palabras)
print("consonantes:", consonantes)

