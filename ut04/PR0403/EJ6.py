nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", 
    "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", 
]

nombres_cortos = [nombre for nombre in nombres if len(nombre) <= 4]
print(nombres_cortos)
