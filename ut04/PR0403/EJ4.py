nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", 
    "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", 
]

nombre_usuario = input("Introduce tu nombre: ")
if nombre_usuario in nombres:
    print(nombres[:nombres.index(nombre_usuario)])
else:
    print("No está en la lista")
