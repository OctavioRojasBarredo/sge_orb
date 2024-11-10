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