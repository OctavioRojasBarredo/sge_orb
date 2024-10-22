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