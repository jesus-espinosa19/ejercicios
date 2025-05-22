#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
#e imprima por pantalla si la contraseña introducida por el ususario conincide con la guardada en la variable sin tener en cuenta
#mayuscula y minuscula.

contraseña_guardada = "Contraseña"


contraseña_usuario = input("Ingrese su contraseña: ")

if contraseña_guardada.casefold() == contraseña_usuario.casefold():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

