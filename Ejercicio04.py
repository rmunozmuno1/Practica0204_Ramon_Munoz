### Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
persona = {}
print("Vamos a crear un diccionario con información sobre una persona.")
print("Cuando hayas terminado, escribe salir")
while True:
    clave = input("Introduce el nombre del dato (por ejemplo: 'nombre', 'edad', etc.): ")
    if clave.lower() == 'salir':
        print('Finalizando. Este es el diccionario final:')
        print(persona)
        break
    valor = input(f"Introduce el valor para '{clave}': ")
    persona[clave] = valor
    print('Contenido actual del diccionario:')
    print(persona)