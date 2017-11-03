# Listas FTW!
foods = ["Hamburguesa", "Tacos", "Pasta", "Lasagna"]
print(foods)

# Accesar a elementos
print(foods[0]) # Hamburguesa
print(foods[2]) # Pasta

# Agregar elementos
foods.append("Sushi")
foods.append("Ensalada")
print(foods)

# Eliminar elementos
foods.remove("Ensalada")
print(foods)

# Revisar si un elemento está presente
"Ensalada" in foods # => False
"Sushi" in foods # => True

# Accesar a un grupo de elementos
print(foods[1:3])
print(foods[3:])

# Que pasa si accedo a un elemento no existente?
# print(foods[12]) ! [IndexError: list index out of range]

# Como puedo evitar el error?
foods.get(12)

# Tambien se puede borrar un grupo de elementos en la lista
# del(foods[3:])
# print(foods)

# Listas de lo que sea
item_description = ["Spider-Man", 1982, 1099.99]
print(item_description)
appearances = [True, True, None, False]
print(appearances)
# ! Pero es menos comun ¯\_(ツ)_/¯

# Funciones relacionadas con Listas
print("Hay", len(foods), "comidas en la lista")
print(foods)

for number in range(10):
    if number % 2 == 0:
        print(number)

foods = ["Burger", "Spaghetti", "Lasagna", "Tacos"]
for food in foods:
    print("Shrimp", food)
