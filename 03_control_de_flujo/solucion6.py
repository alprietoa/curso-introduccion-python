# -- coding: utf-8 --

## Ejercicio 
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo a la edad y el nombre. 
# El grupo A está formado por los menores con un nombre anterior a la M en orden alfabético y los mayores de edad con un nombre posterior a la N.
# El grupo B contiene al resto de alumnos. 
# Escribir un programa que pregunte al usuario su nombre y edad, y muestre por pantalla el grupo que le corresponde. 

name = input("¿Cómo te llamas? ")
age = int(input("¿Cuál es tu edad? "))
if age < 18:
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

