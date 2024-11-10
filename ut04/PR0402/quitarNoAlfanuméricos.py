cadena = str(input("Escribe una cadena: "))

def quitar_no_alfanumericos(cadena):
    resultado = ""
    for c in cadena:
        if c.isalnum():
            resultado += c
    return resultado

print(quitar_no_alfanumericos(cadena))
