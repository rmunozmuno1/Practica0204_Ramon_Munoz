###Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
diccionario = {}
while True:
    entrada = input("Introduce palabras en formato 'español:inglés' separadas por comas ('terminar' para finalizar): ")
    if entrada.lower() == "terminar":
        break
    for par in entrada.split(','):
        if ':' in par:
            espanol, ingles = par.split(':')
            diccionario[espanol.strip()] = ingles.strip()
frase = input('Introduce una frase en español para traducir')
traduccion = " ".join([diccionario.get(palabra, palabra) for palabra in frase.split()])
print('\nTraducción:')
print(traduccion)