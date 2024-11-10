cadena = input("Escribe una cadena para convertir a camelCase: ")

def a_camel_case(cadena):
    palabras = cadena.replace('-', ' ').split()
    resultado = palabras[0].lower()
    for p in palabras[1:]:
        resultado += p.capitalize()
    return resultado

print(a_camel_case(cadena))
