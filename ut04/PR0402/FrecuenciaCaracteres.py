cadena = str(input("Escribe una cadena: "))

def frecuencia_caracteres(cadena):
    frecuencias = {}
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias
print(frecuencia_caracteres(cadena))