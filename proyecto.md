``` 
import csv
import datetime

# Lista para almacenar las tareas
tareas = []

# Función para cargar las tareas desde el archivo CSV
def cargar_tareas():
    try:
        # Abrir el archivo CSV en modo lectura
        with open("tareas.csv", "r") as archivo:
            lector = csv.reader(archivo)  # Leer el contenido del archivo
            next(lector)  # Saltar la primera línea (cabecera)
            # Procesar cada tarea en el archivo CSV
            for nombre, prioridad, fecha, completada in lector:
                try:
                    # Convertir cada tarea en un diccionario
                    tareas.append({
                        "Nombre": nombre,
                        "Prioridad": prioridad,
                        "Fecha límite": datetime.date.fromisoformat(fecha),  # Convertir la fecha a tipo datetime
                        "Completada": completada == "True"  # Convertir el estado a booleano
                    })
                except ValueError:
                    print("Error: Formato de fecha inválido en el archivo CSV. Revisando tarea.")
    except FileNotFoundError:
        print("Archivo de tareas no encontrado. Se creará uno nuevo al guardar.")
    except Exception as e:
        print("Error al cargar tareas: " + str(e))

# Función para guardar las tareas en el archivo CSV
def guardar_tareas():
    try:
        # Abrir el archivo CSV en modo escritura
        with open("tareas.csv", "w") as archivo:
            escritor = csv.writer(archivo)
            # Escribir la cabecera
            escritor.writerow(["Nombre", "Prioridad", "Fecha límite", "Completada"])
            # Escribir cada tarea en el archivo
            for tarea in tareas:
                escritor.writerow([
                    tarea["Nombre"], 
                    tarea["Prioridad"], 
                    tarea["Fecha límite"].strftime("%Y-%m-%d"),  # Convertir la fecha a string en formato ISO
                    tarea["Completada"]
                ])
    except Exception as e:
        print("Error al guardar tareas: " + str(e))

# Función para añadir una tarea a la lista
def añadir_tarea():
    try:
        # Solicitar los datos de la nueva tarea
        nombre = input("Nombre: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        prioridad = input("Prioridad (Alta, Media, Baja): ").capitalize()
        if prioridad not in ["Alta", "Media", "Baja"]:
            raise ValueError("Prioridad inválida. Usa Alta, Media o Baja.")
        fecha = datetime.date.fromisoformat(input("Fecha límite (YYYY-MM-DD): "))
        # Añadir la tarea a la lista
        tareas.append({"Nombre": nombre, "Prioridad": prioridad, "Fecha límite": fecha, "Completada": False})
    except ValueError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error inesperado al añadir tarea: " + str(e))

# Función para listar todas las tareas
def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    try:
        # Imprimir todas las tareas
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea["Completada"] else "Pendiente"
            vencida = " (Vencida)" if tarea["Fecha límite"] < datetime.date.today() and not tarea["Completada"] else ""
            fecha_formateada = tarea["Fecha límite"].strftime("%d-%m-%Y")  # Formato de fecha DD-MM-YYYY
            # Imprimir los detalles de la tarea
            print(str(i) + ": " + tarea["Nombre"] + " - " + tarea["Prioridad"] + " - " + 
                  fecha_formateada + " - " + estado + vencida)
    except Exception as e:
        print("Error al listar tareas: " + str(e))

# Función para marcar una tarea como completada
def completar_tarea():
    try:
        listar_tareas()
        indice = int(input("Número de tarea a completar: "))
        if 0 <= indice < len(tareas):
            tareas[indice]["Completada"] = True  # Marcar la tarea como completada
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except Exception as e:
        print("Error al completar tarea: " + str(e))

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        listar_tareas()
        indice = int(input("Número de tarea a eliminar: "))
        if 0 <= indice < len(tareas):
            tareas.pop(indice)  # Eliminar la tarea seleccionada
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except Exception as e:
        print("Error al eliminar tarea: " + str(e))

# Función principal que muestra el menú de opciones
def menu():
    try:
        cargar_tareas()  # Cargar las tareas al iniciar
        while True:
            # Mostrar las opciones del menú
            print("\n1. Añadir tarea\n2. Listar tareas\n3. Completar tarea\n4. Eliminar tarea\n5. Salir")
            opcion = input("Elige una opción: ").strip()
            if opcion == "1":
                añadir_tarea()  # Llamar a la función para añadir tarea
            elif opcion == "2":
                listar_tareas()  # Llamar a la función para listar tareas
            elif opcion == "3":
                completar_tarea()  # Llamar a la función para completar tarea
            elif opcion == "4":
                eliminar_tarea()  # Llamar a la función para eliminar tarea
            elif opcion == "5":
                guardar_tareas()  # Guardar las tareas antes de salir
                print("¡Hasta luego!")  # Mensaje de despedida
                break
            else:
                print("Opción no válida.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")  # Manejar la interrupción por teclado
    except Exception as e:
        print("Error inesperado en el menú: " + str(e))

# Llamar a la función principal para ejecutar el programa
menu()


# Funciones:
# cargar_tareas():

# Carga las tareas desde el archivo tareas.csv. Si el archivo no existe, se muestra un mensaje y no se realiza ninguna acción. Si el archivo tiene errores de formato en las fechas, se maneja la excepción y se muestra un mensaje de advertencia.
# guardar_tareas():

# Guarda las tareas actuales en el archivo tareas.csv. Cada tarea se guarda con su nombre, prioridad, fecha límite y estado de completado. Si ocurre un error al guardar, se maneja la excepción y se muestra un mensaje de error.
# añadir_tarea():

# Permite al usuario ingresar los detalles de una nueva tarea (nombre, prioridad, fecha límite). Si los datos proporcionados son incorrectos o inválidos, se muestran mensajes de error.
# listar_tareas():

# Muestra todas las tareas almacenadas, indicando su nombre, prioridad, fecha límite y si están completadas o vencidas.
# completar_tarea():

# Permite al usuario marcar una tarea como completada, solicitando el número de la tarea a través de un índice. Si el índice es incorrecto, se maneja el error.
# eliminar_tarea():

# Permite al usuario eliminar una tarea de la lista, solicitando el número de la tarea a través de un índice. Si el índice es incorrecto, se maneja el error.
# menu():

# Función principal que muestra el menú de opciones al usuario. Permite elegir entre añadir tarea, listar tareas, completar tarea, eliminar tarea o salir. También maneja interrupciones (Ctrl+C) y errores inesperados durante la ejecución.
# Manejo de Errores:
# FileNotFoundError: Si el archivo tareas.csv no existe, se maneja con un mensaje de advertencia.
# ValueError: Se maneja cuando los datos ingresados no son válidos (por ejemplo, una fecha incorrecta o una prioridad no válida).
# IndexError: Se maneja si el usuario intenta seleccionar un índice fuera del rango de tareas disponibles.
# Exception: Para capturar cualquier otro tipo de error que pueda ocurrir durante la ejecución.
```