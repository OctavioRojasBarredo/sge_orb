palabras = str(input("Introduce unas palabras: "))


def contarPalabras(palabras):
    palabra = palabras.split(" ")
    contador = 0
    for palabrilla in palabra:
        contador = contador + 1
    print("Hay " + str(contador) + " palabras")
contarPalabras(palabras)
