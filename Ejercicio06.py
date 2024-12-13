'''Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. 
Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a en el que la clave de cada alumno/a 
será su NIF, y el valor será otro diccionario con los datos del alumno/a 
(nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo.
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir alumno/a,
(2) Eliminar alumno/a, 
(3) Mostrar alumno/a, 
(4) Listar todo el alumnado, 
(5) Listar alumnado aprobado, 
(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
1 Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
2 Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
3 Preguntar por el NIF del alumno/a y mostrar sus datos.
4 Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
5 Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
6 Terminar el programa.
'''
terminar = False
Datos = {}
def Añadir_Alumno ():
    NIF = input('Introduzca el NIF del alumno')
    Nombre = input('Introduzca el nombre del alumno')
    Tlf = int(input('Introduzca su telefono'))
    correo = input('Introduzca su correo electronico')
    Nota_Dapi = float(input('Introduzca la nota del alumno'))
    if Nota_Dapi < 5:
        Nota_Dapi = False
    else: 
        Nota_Dapi = True
    Alumno = {'Nombre':Nombre,'Tlf':Tlf,'correo':correo,'Nota_Dapi':Nota_Dapi}
    Datos [NIF] = Alumno



'2'
def Eliminar_Alumno ():
    NIF_para_Borrar = input('Introduzca el NIF del alumno que quiere borrar')
    if NIF_para_Borrar in Datos:
        del Datos[NIF_para_Borrar]



'3'
def Mostrar_Datos ():
    NIF_para_mirar = input('Introduzca el NIF del alumno a observar')
    if NIF_para_mirar in Datos:
        print (Datos[NIF_para_mirar])
    else:
        print ('No se encuentra')


'4'
def Mostrar_datos_de_todos_los_alumnos():
    print (Datos)


'5'
def Mostrar_Aprobados():
    for clave,valor in Datos.items():
        if valor['Nota_Dapi']==True:
            print(clave,valor['Nombre'])

while terminar == False:
    Numero_Seleccionado = input('Introduzca uno de estos numeros (1) Añadir alumno/a, (2) Eliminar alumno/a,(3) Mostrar alumno/a, (4) Listar todo el alumnado,Listar alumnado aprobado,(6) Terminar.')
    if Numero_Seleccionado == '1':
        Añadir_Alumno()
    if Numero_Seleccionado == '2':
        Eliminar_Alumno()
    if Numero_Seleccionado == '3':
        Mostrar_Datos()
    if Numero_Seleccionado == '4':
        Mostrar_datos_de_todos_los_alumnos()
    if Numero_Seleccionado == '5':
        Mostrar_Aprobados()
    if Numero_Seleccionado == '6':
        terminar = True
    else:
        print ('Pulse un boton del 1 al 6 por favor')




