#para tributar un determinado impuesto se debe ser mayor de 16años y tener unos ingresos iguales o superiores a 1000e mensuales
#escribir un programa que pregunte al usuario su edad y su ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

try:
    edad = int(input("Ingrese su edad: "))
    ingresos = float(input("Ingrese sus ingresos mensuales en €: "))

    
    if edad > 16 and ingresos >= 1000:
        print("Usted debe tributar")
    else:
        print("Usted no debe tributar")
except ValueError:
    print("Error: Debes ingresar valores numéricos válidos")
