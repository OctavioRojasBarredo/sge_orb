cadena = str(input("Escribe una cadena: "))
resultado = ""
confirmar = False

for letra in cadena:
    if (letra.isupper()):
        letra = letra.lower()
        confirmar = True
    if (letra.islower() and confirmar == False):
        letra = letra.upper()
    confirmar = False
    resultado += letra
print(resultado)