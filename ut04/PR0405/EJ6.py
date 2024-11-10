from functools import reduce
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
positivos = list(map(lambda sublista: list(filter(lambda x: x > 0, sublista)), numeros))
suma = reduce(lambda x, y: x + y, [sum(sublista) for sublista in positivos])
print(suma)
