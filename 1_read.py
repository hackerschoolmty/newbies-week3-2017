# Funciones en python
# Output a pantalla

print("Tercer semana de Hacker School")

# Input
name = input("Cual es tu nombre?")
print("Tu nombre es", name)

# Input de números
age = int(input("Cual es tu edad?"))
height_in_meters = float(input("Cual es tu estatura en metros?"))
print("Edad: ", age, " Estatura: ", height_in_meters, "m", sep="")

# Funciones desde una librería
import random
print("El ganador de un descuento en Reservamos es:", random.randint(1, 10))

# Funciones propias

def say_hello():
    print("Hola!")

say_hello()

def say_this(this):
    print(this)

say_this("Hello!")

# Funciones con valor de retorno

def square_area(side):
    return side * side

print(square_area(10))

def rectangle_area(length, height):
    return length * height

print(rectangle_area(4,5))

import math

def circle_area(radius):
    return math.pi * radius * radius

print(circle_area(4))
