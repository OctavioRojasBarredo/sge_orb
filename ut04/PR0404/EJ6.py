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
