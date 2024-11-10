cadena = str(input("Escribe una cadena: "))

def caracteresRepetidos(cadena):
    cadenaNueva = ""
    letraAnterior = "" 
    
    for letra in cadena:
        if letra != letraAnterior:
            cadenaNueva += letra
        letraAnterior = letra  
    
    return cadenaNueva
resultado = caracteresRepetidos(cadena)
print(resultado)
