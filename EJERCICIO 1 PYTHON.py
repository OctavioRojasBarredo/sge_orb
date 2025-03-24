import os

cod = 1

alumnos = [
    {
        "codigo": "0001",
        "nombre": "a",
        "apellidos": "b",
        "modulos": {"mates": 3, "fisica": 2}
    },
        {
        "codigo": "0002",
        "nombre": "a",
        "apellidos": "b",
        "modulos": {"mates": 9, "fisica": 2}
    },
        {
        "codigo": "0003",
        "nombre": "a",
        "apellidos": "b",
        "modulos": {"mates": 8, "fisica": 2}
    },
        {
        "codigo": "0004",
        "nombre": "a",
        "apellidos": "b",
        "modulos": {"mates": 3, "fisica": 2}
    }
    
]
modulos = ["mates"]


def registrar_modulo(nuevo):
    if nuevo not in modulos:
        modulos.append(nuevo)
        print("Módulo insertado.")
    else:
        print("Ya existe ese módulo")

def ver_modulos():
    print("Módulos disponibles: ")
    for modulo in modulos:
        print(modulo)

def eliminar_modulo(modulo):
    if modulo in modulos:
        modulos.remove(modulo)
        print("Módulo eliminado.")
    else:
        print("No existe ese módulo")
def matricular_alumno(nombre, apellidos, mod_lst):
    mod = {}
    for i in range (len(mod_lst)):
        mod.update({mod_lst[i]: 0})
    global cod
    cod += 1
    nuevo_alumno = {
                    "codigo": "000" + str(cod),
                    "nombre": nombre,
                    "apellidos": apellidos,
                    "modulos": mod
                }
    alumnos.append(nuevo_alumno)
    
def eliminar_alumno(codigo):
    contador = -1
    for alumno in alumnos:
        contador += 1
        if alumno["codigo"] == codigo:
            alumnos.pop(contador)
            print("Eliminado correctamente.")

def introducir_nota(codigo, modulo, nota):
    existe = False
    for alumno in alumnos:
        if alumno["codigo"] == codigo:
            for mod, no in alumno["modulos"].items():
                if modulo == mod:
                    existe = True
                    no = nota
                    alumno["modulos"][mod] = no
                    print("Nota ingresada correctamente.")
            if not existe:
                print("El alumno no tiene ese módulo.")

    if not existe:
        print("No existe alumno con ese código.")
            

def mostrar_alumnos():
    if alumnos:
        for i in range (len(alumnos)):
            print("\n")
            print("Código: " + alumnos[i]["codigo"])
            print("Nombre: " + alumnos[i]["nombre"])
            print("Apellidos: " + alumnos[i]["apellidos"])
            print("Modulos y notas: ")
            for modulo, nota in alumnos[i]["modulos"].items():
                print(modulo + ": " + str(nota))
    else:
        print("No hay alumnos matriculados.")

def informacion_alumno(codigo):
    contador = -1
    if alumnos:
        for alumno in alumnos:
            contador += 1
            if alumno["codigo"] == codigo:
                print("Código: " + alumnos[contador]["codigo"])
                print("Nombre: " + alumnos[contador]["nombre"])
                print("Apellidos: " + alumnos[contador]["apellidos"])
                print("Modulos y notas: ")
                for modulo, nota in alumnos[contador]["modulos"].items():
                    print(modulo + ": " + str(nota))
    else:
        print("No hay alumnos matriculados.")
def estadisticas(modulo):
    nota_media = 0
    mejor_nota = 0
    peor_nota = 10
    aprobados = 0
    suspensos = 0
    mediana = 0

    notas_lst = []
    for alumno in alumnos:
        for mod, nota in alumno["modulos"].items():
            if mod == modulo:
                notas_lst.append(nota)
                if nota > mejor_nota:
                    mejor_nota = nota
                if nota < peor_nota:
                    peor_nota = nota
                if nota >= 5:
                    aprobados += 1
                else:
                    suspensos += 1
    
    
    # Nota media
    nota_media = sum(notas_lst) / len(notas_lst)
    print("Nota media: " + str(nota_media))
    # Mejor nota
    print("Mejor nota: " + str(mejor_nota))
    # Peor nota
    print("Peor nota: " + str(peor_nota))
    # Aprobados 
    print("Aprobados: " + str(aprobados))
    # Suspensos 
    print("Suspensos: " + str(suspensos))
    # Mediana
    notas_lst.reverse()
    if len(notas_lst) % 2 != 0:
        mediana = notas_lst[len(notas_lst) // 2]
    else:
        num1 = notas_lst[len(notas_lst) // 2]
        num2 = notas_lst[(len(notas_lst) // 2) + 1]
        mediana = (num1 + num2) / 2
    print("Mediana: " + str(mediana))
    
    


while True:
    # os.system("1cls")
    print("EXAMEN DAM - 1ª EVALUACIÓN")
    print("==========================")
    print("  1.- Registrar módulo")
    print("  2.- Ver módulos")
    print("  3.- Eliminar módulo")
    print("  4.- Matricular alumno")
    print("  5.- Eliminar alumno")
    print("  6.- Introducir nota")
    print("  7.- Mostrar alumnos")
    print("  8.- Información de alumno")
    print("  9.- Estadísticas")
    print("")
    op = input("Escoge una opción: ")

    match op:
        case "1": 
            while True:
                nuevo = input("Indica el nuevo módulo: ")
                if nuevo:
                    break
                else:
                    print("No puedes escribirlo vacío.")
            registrar_modulo(nuevo)
            os.system("Pause")
        case "2": 
            ver_modulos()
            os.system("Pause")
        case "3":
            nuevo = input("Indica el módulo a eliminar: ")
            eliminar_modulo(nuevo)
            os.system("Pause")
        case "4": 
            while True:
                nombre = input("Dime el nombre del alumno: ")
                if nombre:
                    break
                else:
                    print("No puedes escribirlo vacío.")
    
            while True:
                apellidos = input("Dime los apellidos del alumno: ")
                if apellidos:
                    break
                else:
                    print("No puedes escribirlo vacío.")
            mod_lst = []
            while True:
                modulo = input("Dime un módulo del alumno ('exit' para acabar de ponerlos): ")
                if modulo:
                    if modulo != "exit":
                        if modulo in modulos:
                            mod_lst.append(modulo) 
                            print("Módulo agregado al alumno.")
                        else:
                            print("El módulo no existe.")
                    else:
                        break
                else:
                    print("No puedes escribirlo vacío.")
            matricular_alumno(nombre, apellidos, mod_lst)
            os.system("Pause")
        case "5":
            while True:
                existe = False
                codigo = input("Dime el codigo del alumno: ")
                if codigo:
                    i = -1
                    for alumno in alumnos:
                        i += 1
                        if alumno["codigo"] == codigo:
                            existe = True
                    if (i + 1) == len(alumnos):
                        if not existe:
                            print("No existe ese código, prueba con otro.")
                        else:
                            break
                else:
                    print("Inserta un código válido.")

            eliminar_alumno(codigo)
            os.system("Pause")
        case "6": 
            while True:
                existe = False
                codigo = input("Dime el codigo del alumno: ")
                if codigo:
                    i = -1
                    for alumno in alumnos:
                        i += 1
                        if alumno["codigo"] == codigo:
                            existe = True
                    if (i + 1) == len(alumnos):
                        if not existe:
                            print("No existe ese código, prueba con otro.")
                        else:
                            break
                else:
                    print("Inserta un código válido.")

            while True:
                existe = False
                mod = input("Dime el modulo del alumno: ")
                for modulo in modulos:
                    if mod:
                        if modulo == mod:
                            existe = True
                    else:
                        print("No has ingresado ningún módulo.")
                if existe:
                    break
                else:
                    print("El módulo ingresado no existe. Prueba con otro.")
                
            while True:
                nota = input("Dime la nota del alumno ")
                if nota:
                    if int(nota) >= 0 and int(nota) <= 10:
                        break
                    else:
                        print("Nota no válida (0-10)")
                else:
                    print("Ingresa una nota.")

            introducir_nota(codigo, mod, nota)

            os.system("Pause")
        case "7":
            mostrar_alumnos()
            os.system("Pause")
        case "8":
            codigo = input("Inserta un código: ")
            while True:
                if codigo:
                        i = -1
                        for alumno in alumnos:
                            i += 1
                            if alumno["codigo"] == codigo:
                                existe = True
                        if (i + 1) == len(alumnos):
                            if not existe:
                                print("No existe ese código, prueba con otro.")
                            else:
                                break
                else:
                    print("Inserta un código válido.")

            informacion_alumno(codigo)
            os.system("Pause")
        case "9":
            while True:
                existe = False
                mod = input("Dime el modulo del alumno: ")
                for modulo in modulos:
                    if mod:
                        if modulo == mod:
                            existe = True
                    else:
                        print("No has ingresado ningún módulo.")
                if existe:
                    break
                else:
                    print("El módulo ingresado no existe. Prueba con otro.")
            estadisticas(mod)
        case _:
            print("")
            x=input("Opción no válida.")
            os.system("Pause")