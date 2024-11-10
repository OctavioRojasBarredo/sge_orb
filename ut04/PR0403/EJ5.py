nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", 
    "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", 
]

longitud_usuario = int(input("Introduce un número para contar nombres de esa longitud: "))
nombres_longitud = [nombre for nombre in nombres if len(nombre) == longitud_usuario]
print(len(nombres_longitud))
