# EJERCICIO 1
```
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
```
# EJERCICIO 2
```
cadena = str(input("Introduce una cadena: "))

print(cadena[::-1])
```
# EJERCICIO 3
```
cadena = str(input("Dime una cadena: "))
cadenaInvertida = cadena[::-1]

if (cadena == cadenaInvertida):
    print("La palabra es palíndroma")
else:
    print("La palabra no es palíndroma")
```
# EJERCICIO 4
```
palabras = str(input("Introduce unas palabras: "))


def contarPalabras(palabras):
    palabra = palabras.split(" ")
    contador = 0
    for palabrilla in palabra:
        contador = contador + 1
    print("Hay " + str(contador) + " palabras")
contarPalabras(palabras)

```
# EJERCICIO 5
```
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

```
# EJERCICIO 6
```
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
```
# EJERCICIO 7
```
cadena = str(input("Introduce una cadena: "))

print(cadena[::-1])
```
# EJERCICIO 8
```
palabra1 = str(input("Introduce una palabra: "))
palabra2 = str(input("Introduce otra palabra: "))
anagrama = False

for letra in palabra1:
    for letra2 in palabra2:
        if (letra in letra2):
            anagrama = True
        elif(anagrama != True):
            anagrama = False
if (anagrama == True):
    print("La palabra " + palabra1 + " y la palabra " + palabra2 + " son anagramas")
else:
    print("La palabra " + palabra1 + " y la palabra " + palabra2 + " no son anagramas")
```
# EJERCICIO 9
```
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
```
# EJERCICIO 10
```
str="Hola mundo que tal"
lista=str.lower().split("")
res=lista[0]
for palabra in lista[1:]:
        res += palabra.title
print(res)
```
# EJERCICIO 11
```
cadena = input("Escribe una cadena para convertir a camelCase: ")

def a_camel_case(cadena):
    palabras = cadena.replace('-', ' ').split()
    resultado = palabras[0].lower()
    for p in palabras[1:]:
        resultado += p.capitalize()
    return resultado

print(a_camel_case(cadena))

```
# EJERCICIO 12
```
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
```