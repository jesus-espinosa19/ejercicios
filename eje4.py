#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ").strip().title()
sexo = input("Ingrese su sexo (M/F): ").strip().upper()


if sexo == "F" and nombre[0] < "M":
    grupo = "A"
elif sexo == "M" and nombre[0] > "N":
    grupo = "A"
else:
    grupo = "B"


print(f"Usted pertenece al grupo {grupo}")