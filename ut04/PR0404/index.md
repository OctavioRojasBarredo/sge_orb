# EJERCICIO 1
```
frutas = {
    "manzana": 1.2,
    "banana": 0.5,
    "pera": 0.8,
    "uva": 2.0
}
fruta_usuario = input("Introduce el nombre de una fruta: ")
print(frutas.get(fruta_usuario, "Fruta no disponible"))

```

# EJERCICIO 2
```
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

for categoria, productos_lista in productos.items():
    print(f"{categoria}: {len(productos_lista)} productos")

print("Total de categorías:", len(productos))
print("Total de productos:", sum(len(productos_lista) for productos_lista in productos.values()))

```

# EJERCICIO 3
```
frase = input("Introduce una frase: ")
palabras = frase.split()
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print(frecuencias)

```

# EJERCICIO 4
```
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

def listar_estudiantes():
    asignatura = input("Introduce el nombre de la asignatura: ")
    if asignatura in asignaturas:
        print(asignaturas[asignatura])
    else:
        print("Asignatura no encontrada")

def matricular_estudiante():
    asignatura = input("Introduce el nombre de la asignatura: ")
    estudiante = input("Introduce el nombre del estudiante: ")
    if asignatura in asignaturas:
        asignaturas[asignatura].append(estudiante)
        print(f"{estudiante} matriculado en {asignatura}")
    else:
        print("Asignatura no encontrada")

def dar_baja_estudiante():
    asignatura = input("Introduce el nombre de la asignatura: ")
    estudiante = input("Introduce el nombre del estudiante: ")
    if asignatura in asignaturas and estudiante in asignaturas[asignatura]:
        asignaturas[asignatura].remove(estudiante)
        print(f"{estudiante} dado de baja de {asignatura}")
    else:
        print("Estudiante o asignatura no encontrados")

print("Menú:")
print("1. Listar estudiantes matriculados en una asignatura")
print("2. Matricular un estudiante")
print("3. Dar de baja un estudiante")

opcion = int(input("Elige una opción: "))
if opcion == 1:
    listar_estudiantes()
elif opcion == 2:
    matricular_estudiante()
elif opcion == 3:
    dar_baja_estudiante()
else:
    print("Opción no válida")

```

# EJERCICIO 5
```
def diccionario_invertido(diccionario):
    return {v: k for k, v in diccionario.items()}

diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(diccionario_invertido(diccionario))

```

# EJERCICIO 6
```
productos1 = {
    "manzana": 1.2,
    "banana": 0.5,
    "pera": 0.8
}
productos2 = {
    "banana": 0.4,
    "uva": 2.0,
    "pera": 1.0
}

productos_combinados = {}

for producto, precio in productos1.items():
    productos_combinados[producto] = productos_combinados.get(producto, 0) + precio

for producto, precio in productos2.items():
    productos_combinados[producto] = productos_combinados.get(producto, 0) + precio

print(productos_combinados)

```
