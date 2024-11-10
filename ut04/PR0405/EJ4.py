palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
palabras_largas = list(map(lambda p: p.upper(), filter(lambda p: len(p) > 5, palabras)))
print(palabras_largas)
