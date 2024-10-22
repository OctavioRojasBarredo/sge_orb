import random

elecciones = {"piedra", "papel", "tijeras"}

victorias_player = 0
victorias_enemigo = 0

while(victorias_player < 5 and victorias_enemigo < 5):
    eleccion_player = input("Elige tu jugada: ")
    eleccion_enemigo = random.choice(list(elecciones))

    match(eleccion_player):
        case "piedra":
            if eleccion_enemigo == "tijeras":
                victorias_player += 1
                print("Gana el jugador (piedra rompe tijeras)")
            elif eleccion_enemigo == "lagarto":
                victorias_player += 1
                print("Gana el jugador (piedra aplasta lagarto)")
            elif eleccion_enemigo == "papel":
                victorias_enemigo += 1
                print("Pierde el jugador (papel envuelve piedra)")
            elif eleccion_enemigo == "spock":
                victorias_enemigo += 1
                print("Pierde el jugador (spock vaporiza piedra)")
            else:
                print("Empate")
                
        case "papel":
            if eleccion_enemigo == "piedra":
                victorias_player += 1
                print("Gana el jugador (papel envuelve piedra)")
            elif eleccion_enemigo == "spock":
                victorias_player += 1
                print("Gana el jugador (papel desautoriza a spock)")
            elif eleccion_enemigo == "tijeras":
                victorias_enemigo += 1
                print("Pierde el jugador (tijeras cortan papel)")
            elif eleccion_enemigo == "lagarto":
                victorias_enemigo += 1
                print("Pierde el jugador (lagarto come papel)")
            else:
                print("Empate")
                
        case "tijeras":
            if eleccion_enemigo == "papel":
                victorias_player += 1
                print("Gana el jugador (tijeras cortan papel)")
            elif eleccion_enemigo == "lagarto":
                victorias_player += 1
                print("Gana el jugador (tijeras decapitan al lagarto)")
            elif eleccion_enemigo == "piedra":
                victorias_enemigo += 1
                print("Pierde el jugador (piedra rompe tijeras)")
            elif eleccion_enemigo == "spock":
                victorias_enemigo += 1
                print("Pierde el jugador (spock rompe tijeras)")
            else:
                print("Empate")
                
        case "lagarto":
            if eleccion_enemigo == "papel":
                victorias_player += 1
                print("Gana el jugador (lagarto come papel)")
            elif eleccion_enemigo == "spock":
                victorias_player += 1
                print("Gana el jugador (lagarto envenena a spock)")
            elif eleccion_enemigo == "piedra":
                victorias_enemigo += 1
                print("Pierde el jugador (piedra aplasta lagarto)")
            elif eleccion_enemigo == "tijeras":
                victorias_enemigo += 1
                print("Pierde el jugador (tijeras decapitan al lagarto)")
            else:
                print("Empate")
                
        case "spock":
            if eleccion_enemigo == "tijeras":
                victorias_player += 1
                print("Gana el jugador (spock rompe tijeras)")
            elif eleccion_enemigo == "piedra":
                victorias_player += 1
                print("Gana el jugador (spock vaporiza piedra)")
            elif eleccion_enemigo == "papel":
                victorias_enemigo += 1
                print("Pierde el jugador (papel desautoriza a spock)")
            elif eleccion_enemigo == "lagarto":
                victorias_enemigo += 1
                print("Pierde el jugador (lagarto envenena a spock)")
            else:
                print("Empate")
                
        case _:
            print("Elección no válida, intenta de nuevo")
if (victorias_enemigo == 5):
    print("Ganó el enemigo")
else:
    print("Ganó el jugador")