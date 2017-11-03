# Escribe una aplicacion para el menu intelitente de un restaurante
# Este menu tiene 2 opciones
# a. Ingresar un nuevo item
# b. Ver todos los items
#
# Item Ejemplo:
# name: Tacos de Barbacoa
# price: 100.0
# calories: 3000
# category: Desayuno

option_prompt = """
Ingresa la opción deseada:

a. Nuevo item
b. Imprimir menu
c. Salir
-> """

def get_option():
    option = input(option_prompt)
    if option in ['a', 'b', 'c']:
        return option
    else:
        get_option()

def main():
    option = get_option()
    while True:
        if option == 'a':
            print("Do something")
        elif option == 'b':
            print("Do something else")
        else:
            return
        option = get_option()

main()
