### Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario
moneda = input('¿Que divisa utilizas?')
Dicti = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
if moneda.title in Dicti.keys():
    print (Dicti.get(moneda))
else:
    print ('No se encuentra en el diccionario o intruduzca la primera en mayuscukas')