a = 1
b = 1
resul = 0
cant = int(input("Di cuantos numeros quieres: "))

print(str(a))
print(str(b))

for i in range(3, cant):
    resul = a + b
    a = b
    b = resul
    print(resul)
    