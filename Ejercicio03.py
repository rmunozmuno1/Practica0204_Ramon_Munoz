###Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, pregunte al usuario por un artículo, un número de unidades y muestre por pantalla el precio de esa cantidad de producto. Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.
Lista_de_la_compra = {'Pan':1.40, 'Huevos':2.30, 'Cebolla':0.85, 'Aceite':4.35}
Eleccion = input('Que quieres comprar')
if Eleccion in Lista_de_la_compra.keys():
    cantidad = int(input('Cantidad del producto'))
    print (Lista_de_la_compra.get(Eleccion) * cantidad)