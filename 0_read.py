# Repaso rapido variables y condiciones
# Presentacion
name = "Adrian"
age = 31
loves_running = True
running_km_per_hour = 11.6
height_in_meters = 1.6
loves_despacito_song = False
preferred_mexican_tv_channel = None

# Operaciones matematicas
current_year = 2017
meters_to_the_moon = 384400000000

print("Adrian nacio el año", 2017 - age)
print("Caben ", meters_to_the_moon / height_in_meters, "Adrianes de aquí a la luna")

# Condicionales sencillos
if loves_despacito_song:
    print("No mas cervezas para Adrian")
else:
    print("Adrian tiene un gusto decente en la musica")

# Condicionales
if age <= 18:
    print("Adrian es un Generacion Z")
elif age <= 32:
    print("Adrian es un Millenial")
else:
    print("Adrian es un Generacion X")

# Ciclos
# print("La historia de Adrian: ")
# year = 1
#
# while year <= age:
#     print("Adrian cumple ", year, "años")
#     year += 1
