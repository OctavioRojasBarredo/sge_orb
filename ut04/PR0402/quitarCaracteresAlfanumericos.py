str="Hola mundo que tal"
lista=str.lower().split("")
res=lista[0]
for palabra in lista[1:]:
        res += palabra.title
print(res)