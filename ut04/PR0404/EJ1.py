frutas = {
    "manzana": 1.2,
    "banana": 0.5,
    "pera": 0.8,
    "uva": 2.0
}
fruta_usuario = input("Introduce el nombre de una fruta: ")
print(frutas.get(fruta_usuario, "Fruta no disponible"))
