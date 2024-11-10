cadena = str(input("Escribe varias palabras: "))

cadena = cadena.split(" ")
resultado = ""
n = len(cadena)

while (n != 0):
    n -= 1
    resultado += cadena[n] + " "
print(resultado)