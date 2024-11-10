def rle(cadena):
    resultado = ""
    contador = 1
    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i - 1]:
            contador += 1
        else:
            resultado += cadena[i - 1] + str(contador)
            contador = 1
    resultado += cadena[-1] + str(contador) 
    return resultado

cadena = input("Introduce una cadena: ")
print(rle(cadena))
