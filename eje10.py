#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
# otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Ingrese su correo electrónico: ")

nombre_usuario = correo.split("@")[0]

nuevo_correo = f"{nombre_usuario}@ceu.es"

print(f"Nuevo correo electrónico: {nuevo_correo}")