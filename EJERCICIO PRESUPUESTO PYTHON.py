import csv
import os

def agregar_ingreso():
    while True:
        cantidad = input("Indica la cantidad a ingresar: ")
        try:
            cantidad = float(cantidad)
            if cantidad > 0:
                break
            else:
                print("Tienes que ingresar una cantidad mayor que 0.")
        except ValueError:
            print("Inserta un número válido.")

    print("Elige o crea una categoría. ")
    print("Categorías disponibles: ")
    categorias = []
    with open('categorias.csv', mode="r", encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            categorias.append(fila["categorias"])
    print(categorias)
    categoria = input("Categoría: ")
    descripcion = input("Descripción (opcional): ")
    fecha = input("Fecha: ")
    with open('data.csv', mode="a", encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['cantidad', 'categoria', 'descripcion', 'fecha'])
        escritor.writerow({'cantidad': cantidad, 'categoria': categoria, 'descripcion': descripcion, 'fecha': fecha})
    if categoria not in categorias:
        with open('categorias.csv', mode="a", encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(categoria)


def agregar_gasto():
    ""
def resumen_mensual():
    ""
def resumen_anual():
    ""
def ingresos_por_categoria():
    ""
def gastos_por_categoria():
    ""
def guardar():
    ""
def cargar():
    ""
def salir():
    ""

while True:
    # os.system("1cls")
    print("EXAMEN DAM - 1ª EVALUACIÓN")
    print("==========================")
    print("  1.- Agregar ingreso")
    print("  2.- Agregar un gasto")
    print("  3.- Mostrar resumen de un mes")
    print("  4.- Generar resumen mensual")
    print("  5.- Ingresos por categoría")
    print("  6.- Gastos por categoría")
    print("  7.- Guardar en archivo")
    print("  8.- Cargar archivo")
    print("  9.- Salir")
    print("")
    op = input("Escoge una opción: ")

    match op:
        case "1": 

    
            agregar_ingreso()
            os.system("Pause")
        case "2": 
            lst = get_usernames()
            print( lst )
            os.system("Pause")
        case "3":
            subject = input("Indica el código de una asignatura: ")
            lst = get_by_subject(subject)
            print( lst )
            os.system("Pause")
        case "4": 
            nif     = input("Dime el NIF del alumno: ")
            subject = input("Dime la asignatura: ")
            grade   = input("Dime la nota: ")
            data = set_grade(nif, subject, grade, data)

            for alumno in data:
                if alumno["nif"] == nif:
                    print(alumno)
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
            data_by_subject = get_list_by_subject()
            print(data_by_subject)
            os.system("Pause")
        case _:
            print("")
            x=input("Opción no válida.")
            os.system("Pause")