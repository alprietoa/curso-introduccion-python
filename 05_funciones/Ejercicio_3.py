# -- coding: utf-8 --
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


print(celsius_a_fahrenheit(0))      # 32.0
print(fahrenheit_a_celsius(32))     # 0.0