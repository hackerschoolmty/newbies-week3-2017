# Funciones

## Modelos mentales

¿Qué entendemos cuando escuchamos la palabra **Función**?

* Una tarea - Podar el cesped (¿Funciona o no funciona?)
* Un rol - La función de un programador es crear software para una empresa

En este caso se parece a ambos aunque se parece mucho más a la primera.

¿ Qué es una función ?

```
Las funciones son mini programas que nos ayudan a realizar una tarea específica.
```

Las funciones interactuan con nuestro programa así:

1. Reciben un input
2. Realizan una tarea específica
3. Regresan un output

¿ Qué es lo más importante de una función ?

* Su nombre
* Sus parámetros (input)
* Su valor de retorno (output)

```python
		def increment (number):
			result = number + 1
			return result
```

* Nombre: `increment`
* Parámetros: `number` (Más que el nombre nos importa lo que significa)
* Valor de returno: `result` (En este caso no nos importa el nombre pero sí que significa ese resultado)

### Ejemplos de funciones del lenguaje

```python
	print()

	input()

	len()

	range()
```

### Una guía para crear buenas funciones

* Escoger nombres explícitos y fácil de entender

```python
def average_between_dates (start_date, end_date):

# VS

def avg_in (a, b):
```

* Hace solo una tarea y es fácil comunicarla a través del nombre

```python
	def apply_discount (amount):

	# VS

	def discount_save_and_email():
```

* ¿ Cuantos parámetros debe tener ?

	* 1 = Excelente
	* 2 = Bien
	* 3 = Cuestionate si tu función tiene demasiada responsabilidad

* Tu función no tiene **efectos secundarios**

	* `get_total` calcula el total y al mismo tiempo aplica los descuento disponibles.
