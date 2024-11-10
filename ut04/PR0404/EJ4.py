asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

def listar_estudiantes():
    asignatura = input("Introduce el nombre de la asignatura: ")
    if asignatura in asignaturas:
        print(asignaturas[asignatura])
    else:
        print("Asignatura no encontrada")

def matricular_estudiante():
    asignatura = input("Introduce el nombre de la asignatura: ")
    estudiante = input("Introduce el nombre del estudiante: ")
    if asignatura in asignaturas:
        asignaturas[asignatura].append(estudiante)
        print(f"{estudiante} matriculado en {asignatura}")
    else:
        print("Asignatura no encontrada")

def dar_baja_estudiante():
    asignatura = input("Introduce el nombre de la asignatura: ")
    estudiante = input("Introduce el nombre del estudiante: ")
    if asignatura in asignaturas and estudiante in asignaturas[asignatura]:
        asignaturas[asignatura].remove(estudiante)
        print(f"{estudiante} dado de baja de {asignatura}")
    else:
        print("Estudiante o asignatura no encontrados")

print("Menú:")
print("1. Listar estudiantes matriculados en una asignatura")
print("2. Matricular un estudiante")
print("3. Dar de baja un estudiante")

opcion = int(input("Elige una opción: "))
if opcion == 1:
    listar_estudiantes()
elif opcion == 2:
    matricular_estudiante()
elif opcion == 3:
    dar_baja_estudiante()
else:
    print("Opción no válida")
