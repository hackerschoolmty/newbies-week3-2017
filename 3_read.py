# Diccionarios
# Diccionario simple
fruit = { "name": "Manzana", "color": "roja" }

# Acceder a los datos con la llave
print(fruit["name"])
print(fruit["color"])

# Acceder datos libre de errores
print(fruit.get('size')) # => None

# Agregar datos
fruit["calories"] = 52
fruit["weight"] = 100

# Los diccionarios tambien pueden contener listas
fruit["vitamins"] = ["A", "C"]
print(fruit)

# Eliminar datos
del(fruit["weight"])
print(fruit)

# Diccionario con mútiples tipos de dato
# Navegar a traves de los datos de un diccionario:
print("Propiedades de la manzana:")
for name, value in fruit.items():
    print(name + ':', value)

# Una lista de diccionarios
fruits = [
    { "name": "Manzana", "color": "roja" },
    { "name": "Naranja", "color": "naranja"},
    { "name": "Limon", "color": "verde" }
]

for fruit in fruits:
    print(fruit["name"], "es de color", fruit["color"])
