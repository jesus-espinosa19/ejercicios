#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
# es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla 
# el número de teléfono sin el prefijo y la extensión.

telefono = input("Ingrese su número de teléfono (+34-xxxxxxxxx-xx): ")

partes = telefono.split("-")

numero_sin_prefijo_extension = partes[1]
print(f"Número de teléfono sin prefijo y extensión: {numero_sin_prefijo_extension}")
