palabra = str(input("Di una palabra: "))

def vocalesConsonantes(palabra):
    vocales = str("aeiouAEIOUáéíóúÁÉÚÍÓ")
    contadorVocales = 0
    contadorConsonantes = 0
    for letra in palabra:
        if letra in vocales:
            contadorVocales += 1
        else:
            contadorConsonantes += 1
    print("Cantidad vocales: " + str(contadorVocales))
    print("Cantidad consonantes: " + str(contadorConsonantes))

vocalesConsonantes(palabra)