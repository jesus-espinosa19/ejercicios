#Escribir un programa que pida al usuario dos numeros y muestre por pantalla su division.
#si el divisor es cero el programa debe mostrar un error.


try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))

    
    if divisor == 0:
        print("Error: No se puede dividir por cero")
    else:
        
        resultado = dividendo / divisor
        print(f"{dividendo} dividido por {divisor} es igual a {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido")