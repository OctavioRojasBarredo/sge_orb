# EJERCICIO 1

```
from random import *
numeroRandom = randint(0, 100)
numeroElegido = int(input("Di un número: "))

while (numeroElegido != numeroRandom):
    if (numeroElegido < numeroRandom):
        print("Incorrecto. El número es mayor")
    if (numeroElegido > numeroRandom):
        print("Incorrecto. El número es menor")
    numeroElegido = int(input("Di un número: "))

print("Correcto! El número era: " + str(numeroRandom))
```

# EJERCICIO 2

```
numero = int(input("Dime un número: "))
tabla = int(input("Dime la tabla de multiplicación: "))
resul = 0
contador = 0

while (contador < numero):
    contador = contador + 1
    resul = tabla * contador
    print(resul)

```

# EJERCICIO 3

```
num = int(input("Dime un número: "))
while (num % 2 != 0):
    num = int(input("El número es impar, dime un número par: "))
asterisco = "*"
espacios = ""
totalAsteriscos = ""
for i in range(1, num+1, 2):
    espacios = (num-i) / 2
    totalAsteriscos += asterisco
    print(" " * int(espacios) + "*" * i)

```

# EJERCICIO 4

```
num = int(input("Dime un número: "))
while (num % 2 != 0):
    num = int(input("El número es impar, dime un número par: "))
asterisco = "*"
espacios = ""
totalAsteriscos = ""
for i in range(1, num+1, 2):
    espacios = (num-i) / 2
    totalAsteriscos += asterisco
    print(" " * int(espacios) + "*" * i)

```

# EJERCICIO 5

```
import math

mayorNumero = 0
menorNumero = math.inf
i = 0

for i in range(0, 5, i+1):
    num = int(input("Dame un número: "))
    if (num > mayorNumero):
        mayorNumero = num
    if (num < menorNumero):
        menorNumero = num
print("El mayor número es: "+mayorNumero)
print("El menor número es: "+menorNumero)
```

# EJERCICIO 6

```
cantidad = float(input("Introduce la cantidad: "))
unidad = str(input("Introduce la unidad de medida (mm, cm, m, km): "))
unidadConvertir = str(input("Introduce la unidad de medida a la que quieras convertir (mm, cm, m, km): "))

match(unidad):
    case "mm":
        resultado = cantidad / (10 if unidadConvertir == "cm" else 
                                1000 if unidadConvertir == "m" else 
                                1000000 if unidadConvertir == "km" else 
                                1)
    case "cm":
        resultado = cantidad / (0.1 if unidadConvertir == "mm" else 
                                100 if unidadConvertir == "m" else 
                                100000 if unidadConvertir == "km" else 
                                1)
    case "m":
        resultado = cantidad / (0.001 if unidadConvertir == "mm" else 
                                0.01 if unidadConvertir == "cm" else 
                                1000 if unidadConvertir == "km" else 
                                1)
    case "km":
        resultado = cantidad / (0.000001 if unidadConvertir == "mm" else 
                                0.00001 if unidadConvertir == "cm" else 
                                0.001 if unidadConvertir == "m" else 
                                1)
    case _:
        resultado = "Unidad no reconocida."

print(str(cantidad) + "en " + str(unidad) + " es igual a " + str(resultado) + " " + str(unidadConvertir))
```

# EJERCICIO 7

```
from random import *
numeroRandom = randint(0, 100)
numeroElegido = int(input("Di un número: "))

while (numeroElegido != numeroRandom):
    if (numeroElegido < numeroRandom):
        print("Incorrecto. El número es mayor")
    if (numeroElegido > numeroRandom):
        print("Incorrecto. El número es menor")
    numeroElegido = int(input("Di un número: "))

print("Correcto! El número era: " + str(numeroRandom))

```

# EJERCICIO 8

```
import random

elecciones = {"piedra", "papel", "tijeras"}

victorias_player = 0
victorias_enemigo = 0

while(victorias_player < 5 and victorias_enemigo < 5):
    eleccion_player = input("Elige tu jugada: ")
    eleccion_enemigo = random.choice(list(elecciones))

    match(eleccion_player):
        case "piedra":
            if eleccion_enemigo == "tijeras":
                victorias_player += 1
                print("Gana el jugador (piedra rompe tijeras)")
            elif eleccion_enemigo == "lagarto":
                victorias_player += 1
                print("Gana el jugador (piedra aplasta lagarto)")
            elif eleccion_enemigo == "papel":
                victorias_enemigo += 1
                print("Pierde el jugador (papel envuelve piedra)")
            elif eleccion_enemigo == "spock":
                victorias_enemigo += 1
                print("Pierde el jugador (spock vaporiza piedra)")
            else:
                print("Empate")
                
        case "papel":
            if eleccion_enemigo == "piedra":
                victorias_player += 1
                print("Gana el jugador (papel envuelve piedra)")
            elif eleccion_enemigo == "spock":
                victorias_player += 1
                print("Gana el jugador (papel desautoriza a spock)")
            elif eleccion_enemigo == "tijeras":
                victorias_enemigo += 1
                print("Pierde el jugador (tijeras cortan papel)")
            elif eleccion_enemigo == "lagarto":
                victorias_enemigo += 1
                print("Pierde el jugador (lagarto come papel)")
            else:
                print("Empate")
                
        case "tijeras":
            if eleccion_enemigo == "papel":
                victorias_player += 1
                print("Gana el jugador (tijeras cortan papel)")
            elif eleccion_enemigo == "lagarto":
                victorias_player += 1
                print("Gana el jugador (tijeras decapitan al lagarto)")
            elif eleccion_enemigo == "piedra":
                victorias_enemigo += 1
                print("Pierde el jugador (piedra rompe tijeras)")
            elif eleccion_enemigo == "spock":
                victorias_enemigo += 1
                print("Pierde el jugador (spock rompe tijeras)")
            else:
                print("Empate")
                
        case "lagarto":
            if eleccion_enemigo == "papel":
                victorias_player += 1
                print("Gana el jugador (lagarto come papel)")
            elif eleccion_enemigo == "spock":
                victorias_player += 1
                print("Gana el jugador (lagarto envenena a spock)")
            elif eleccion_enemigo == "piedra":
                victorias_enemigo += 1
                print("Pierde el jugador (piedra aplasta lagarto)")
            elif eleccion_enemigo == "tijeras":
                victorias_enemigo += 1
                print("Pierde el jugador (tijeras decapitan al lagarto)")
            else:
                print("Empate")
                
        case "spock":
            if eleccion_enemigo == "tijeras":
                victorias_player += 1
                print("Gana el jugador (spock rompe tijeras)")
            elif eleccion_enemigo == "piedra":
                victorias_player += 1
                print("Gana el jugador (spock vaporiza piedra)")
            elif eleccion_enemigo == "papel":
                victorias_enemigo += 1
                print("Pierde el jugador (papel desautoriza a spock)")
            elif eleccion_enemigo == "lagarto":
                victorias_enemigo += 1
                print("Pierde el jugador (lagarto envenena a spock)")
            else:
                print("Empate")
                
        case _:
            print("Elección no válida, intenta de nuevo")
if (victorias_enemigo == 5):
    print("Ganó el enemigo")
else:
    print("Ganó el jugador")
```

# EJERCICIO 9

```
a = 1
b = 1
resul = 0
cant = int(input("Di cuantos numeros quieres: "))

print(str(a))
print(str(b))

for i in range(3, cant):
    resul = a + b
    a = b
    b = resul
    print(resul)
    
```