from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]
producto = reduce(lambda x, y: x * y, map(lambda x: x if x % 2 == 0 else 1, numeros))
print(producto)
