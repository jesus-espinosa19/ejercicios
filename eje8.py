#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla 
# la frase invertida.


frase = input("Ingrese una frase: ")

palabras = frase.split()
print(f"Frase con palabras invertidas: {' '.join(palabras[::-1])}")