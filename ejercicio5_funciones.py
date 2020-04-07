""" Ejercicio 5

    Escribir una función que calcule el área de un círculo 
    y otra que calcule el volumen de un cilindro usando la primera función. """

def cilinder_volumen(radius, high):
    '''
    Función que calcula el volumen de un cilindro 
    parametros:
        radius: Es el radio de la base del cilindro
        high: Es la altura del cilindro
    Devuelve:
        El volumen del cilindro tomando el radius y high
    
    '''
    return circle_area(radius) * high

def circle_area(radius):
    '''
    Función que calcula el area de un circulo
    parametros:
        radius = El radio de un circulo
    Devuelve:
        Devuelve el area del circulo
    '''
    pi = 3.1415

    return 2 * pi * radius ** 2

print(cilinder_volumen(3,5))