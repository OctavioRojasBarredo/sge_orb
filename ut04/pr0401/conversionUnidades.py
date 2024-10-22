cantidad = float(input("Introduce la cantidad: "))
unidad = str(input("Introduce la unidad de medida (mm, cm, m, km): "))
unidadConvertir = str(input("Introduce la unidad de medida a la que quieras convertir (mm, cm, m, km): "))

match(unidad):
    case "mm":
        resultado = cantidad / (10 if unidadConvertir == "cm" else 
                                1000 if unidadConvertir == "m" else 
                                1000000 if unidadConvertir == "km" else 
                                1)
    case "cm":
        resultado = cantidad / (0.1 if unidadConvertir == "mm" else 
                                100 if unidadConvertir == "m" else 
                                100000 if unidadConvertir == "km" else 
                                1)
    case "m":
        resultado = cantidad / (0.001 if unidadConvertir == "mm" else 
                                0.01 if unidadConvertir == "cm" else 
                                1000 if unidadConvertir == "km" else 
                                1)
    case "km":
        resultado = cantidad / (0.000001 if unidadConvertir == "mm" else 
                                0.00001 if unidadConvertir == "cm" else 
                                0.001 if unidadConvertir == "m" else 
                                1)
    case _:
        resultado = "Unidad no reconocida."

print(str(cantidad) + "en " + str(unidad) + " es igual a " + str(resultado) + " " + str(unidadConvertir))
