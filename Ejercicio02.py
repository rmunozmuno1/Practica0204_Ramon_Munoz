### Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”.
Nombre1 = input('Introduzca su nombre')
Edad1 = int(input('Introduzca su edad'))
Direccion1 = input('Introduzca su direccion')
Telefono1 = int(input('Introduzca su telefono'))
Dicccionario = {'Nombre':Nombre1, 'Edad': Edad1, 'Direccion':Direccion1,'Telefono':Telefono1}
print ((Dicccionario['Nombre']), 'tiene',(Dicccionario['Edad']), 'años, vive en',(Dicccionario['Direccion']),'y su numero de telefono es', (Dicccionario['Telefono']))