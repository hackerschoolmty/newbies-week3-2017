# Funciones en python
# Output a pantalla
print("Bienvenidos a la tercer semana de Hacker School")

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
