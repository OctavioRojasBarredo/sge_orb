import os

cod = "0001"

dimensiones = [
    {"nombre": "dimension a", "tecnologia": "malilla", "gravedad": 2.0, 
     "habitantes": [{"nombre": "orbisians"}]}
]

portales = {
    "dimension 1": [],
    "dimension 2": [],
}

habitantes = {
    "dimension": {"raza1": [{"nombre": "orbisians", "habilidades": ["habilidad1", "habilidad2"]}]}
}

reglas = {"dimension": [["50293042", "1238423"], ["9485239", "5823842"]]}

def crear_dimension(nombre, tecnologia, gravedad, habitantes):
    nueva_dimension = {"nombre": nombre, "tecnologia": tecnologia, "gravedad": gravedad, 
     "habitantes": [{"nombre": habitantes}]}
    dimensiones.append(nueva_dimension)

def agregar_portal():
    while True:
        dimension_origen = input("Dime la dimensión de origen: ")
        if dimension_origen:
            if dimension_origen in dimensiones:
                break
            else:
                print("No existe esa dimensión.")
        else:
            print("Introduce una dimensión.")

    while True:
        dimension_destino = input("Dime la dimensión de destino: ")
        if dimension_destino:
            if dimension_destino in dimensiones:
                break
            else:
                print("No existe esa dimensión.")
        else:
            print("Introduce una dimensión.")

    while True:
        estabilidad = input("Introduce su estabilidad (Baja, media o alta): ").lower()
        if estabilidad in ["baja", "media", "alta"]:
            break
        else:
            print("Tienes que introducir baja, media o alta.")

    while True:
        energia_requerida = input("Introduce la energía requerida (máx: 10): ")
        if energia_requerida.isdigit:
            if energia_requerida >= 0 and energia_requerida <= 10:
                break
            else:
                print("Tienes que introducir un número del 0-10.")
        else:
            print("Tienes que introducir un número.")

    portales.append({dimension_origen: [dimension_origen, dimension_destino, estabilidad, energia_requerida]})

def registrar_habitante(dimension, nombre, raza, habilidades):
    while True:
        dimension = input("Dime la dimensión de origen: ")
        if dimension:
            if dimension in dimensiones:
                break
            else:
                print("No existe esa dimensión.")
        else:
            print("Introduce una dimensión.")

    while True:
        nombre = input("Dime el nombre del habitante: ")
        if nombre:
            if not nombre.isdigit:
                break
            else:
                print("Tienes que introducir una cadena de texto.")
        else:
            print("Tienes que introducir un nombre.")

    while True:
        raza = input("Dime la raza del habitante: ")
        if raza:
            if not raza.isdigit:
                break
            else:
                print("Tienes que introducir una cadena de texto.")
        else:
            print("Tienes que introducir un nombre.")

    while True:
        habilidades_lst = []
        habilidades = input("Dime las habilidades que tiene (separado por comas sin espacios): ").split(",")
        if habilidades:
            for habilidades in raza:
                habilidades_lst.append(habilidades)
            break
        else:
            print("Tienes que introducir un nombre.")


    habitantes.append({dimension: {raza: [{"nombre": nombre, "habilidades": habilidades}]}})

    


def definir_reglas_fisicas(dimension, reglas):
    while True:
        dimension = input("Dime la dimensión de origen: ")
        if dimension:
            if dimension in dimensiones:
                break
            else:
                print("No existe esa dimensión.")
        else:
            print("Introduce una dimensión.")

    while True:
        gravedad_lst = []
        gravedad = input("Dime las gravedades que tiene (separado por comas sin espacios): ").split(",")
        if gravedad:
            for grav in gravedad:
                gravedad_lst.append(grav)
            break
        else:
            print("Tienes que introducir una gravedad.")

    while True:
        velocidad_lst = []
        velocidad = input("Dime las velodidades que tiene (separado por comas sin espacios): ").split(",")
        if velocidad:
            for vel in velocidad:
                velocidad_lst.append(vel)
            break
        else:
            print("Tienes que introducir una velocidad.")

    reglas.append({dimension: [gravedad_lst, velocidad_lst]})

    

def listar_dimensiones():
    for dimension in dimensiones:
        print("Nombre: " + dimension["nombre"])
        print("Tecnología: " + dimension["tecnologia"])
        print("Gravedad: " + dimension["gravedad"])
        print("Habitantes: " + dimension[1][habitantes])

def consultar_portales():
    ""

def buscar_habitante():
    ""

def analizar_gravedad():
    ""

def dimension_mas_poblada():
    ""

def eliminar_dimension():
    ""


while True:
    # os.system("1cls")
    print("EXAMEN DAM - 1ª EVALUACIÓN")
    print("==========================")
    print("  1.- Crear dimensión")
    print("  2.- Agregar portal")
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
            nombre = input("Indica el nombre de la dimensión: ")
            tecnologia = input("Indica la tecnología: ")
            gravedad = input("Indica la gravedad: ")
            habitantes = input("Indica el nombre de los habitantes: ")
            crear_dimension(nombre, tecnologia, gravedad, habitantes)
            os.system("Pause")
        case "2": 
            agregar_portal()
            os.system("Pause")
        case "3":
            nuevo = input("Indica el módulo a eliminar: ")
            eliminar_modulo(nuevo)
            os.system("Pause")
        case "4": 
            nombre = input("Dime el nombre del alumno: ")
            apellidos = input("Dime los apellidos del alumno: ")
            matricular_alumno(nombre, apellidos)
            os.system("Pause")
        case "5":
            str = input("Dime un nombre de alumno: ")
            lst = search_student( str )
            print( lst )
            os.system("Pause")
        case "6": 
            str = input("Dime el nombre del módulo: ")
            avg = get_subject_average( str )
            print( avg )
            os.system("Pause")
        case "7":
            mostrar_alumnos()
            os.system("Pause")
        case _:
            print("")
            x=input("Opción no válida.")
            os.system("Pause")