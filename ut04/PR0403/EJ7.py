from collections import Counter

nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", 
    "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", 
]

vocales = "aeiou"
nombres_minusculas = ''.join(nombre.lower() for nombre in nombres)
print({v: nombres_minusculas.count(v) for v in vocales})
