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
            registrar_modulo(nuevo)
            os.system("Pause")
        case "2": 
            ver_modulos()
            os.system("Pause")
        case "3":
            eliminar_modulo(nuevo)
            os.system("Pause")
        case "4": 

            matricular_alumno(nombre, apellidos, mod_lst)
            os.system("Pause")
        case "5":
            eliminar_alumno(codigo)
            os.system("Pause")
        case "6": 
            introducir_nota(codigo, mod, nota)

            os.system("Pause")
        case "7":
            mostrar_alumnos()
            os.system("Pause")
        case "8":
            informacion_alumno(codigo)
            os.system("Pause")
        case "9":
            estadisticas(mod)
        case _:
            print("")
            x=input("Opción no válida.")
            os.system("Pause")