#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ").lower()


while vocal not in "aeiou":
    vocal = input("La vocal ingresada no es válida. Ingrese una vocal (a, e, i, o, u): ").lower()

frase_con_vocal_mayuscula = frase.replace(vocal, vocal.upper())
print(f"Frase con vocal en mayúscula: {frase_con_vocal_mayuscula}")