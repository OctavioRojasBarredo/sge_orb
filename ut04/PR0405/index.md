# EJERCICIO 1
```
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

```

# EJERCICIO 2
```
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)

```

# EJERCICIO 3
```
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)

```

# EJERCICIO 4
```
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
palabras_largas = list(map(lambda p: p.upper(), filter(lambda p: len(p) > 5, palabras)))
print(palabras_largas)

```

# EJERCICIO 5
```
from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]
producto = reduce(lambda x, y: x * y, map(lambda x: x if x % 2 == 0 else 1, numeros))
print(producto)

```

# EJERCICIO 6
```
from functools import reduce
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
positivos = list(map(lambda sublista: list(filter(lambda x: x > 0, sublista)), numeros))
suma = reduce(lambda x, y: x + y, [sum(sublista) for sublista in positivos])
print(suma)

```
