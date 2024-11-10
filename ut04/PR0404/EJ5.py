def diccionario_invertido(diccionario):
    return {v: k for k, v in diccionario.items()}

diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(diccionario_invertido(diccionario))
