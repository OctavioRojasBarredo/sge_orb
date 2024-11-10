frase = input("Introduce una frase: ")
palabras = frase.split()
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print(frecuencias)
