import string

nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", 
    "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", 
]

nombres_minusculas = ''.join(nombre.lower() for nombre in nombres)
print({letra: nombres_minusculas.count(letra) for letra in string.ascii_lowercase})
