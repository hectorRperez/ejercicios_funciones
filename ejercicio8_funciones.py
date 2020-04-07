""" Ejercicio 8
    
    Escribir una función que reciba una muestra de números en una lista 
    y devuelva un diccionario 
    con su media, varianza y desviación típica. """

def promedio_numero(lista_numero):
    '''
    Función que calcula el promedio de una lista de numeros
    parametro:
        lista_numero : Una lista de números
    Devuelve:
        Una lista con los cuadrados de cada numero que recibio por la lista 
        como parametro
    '''
    lista_cuadrado = []

    for i in lista_numero:
        lista_cuadrado.append(i**2)
    
    return lista_cuadrado


def estadistica(lista_numero):
    '''
    Función que calcula la media, varianza y desviación típica de una muestra de números
    parametros: 
        lista_numero: Es una lista de números
    Devuelve:
        Un diccionario con la media, varianza y desviación tipica de los números de 
        lista_numero
    '''

    stat = {}
    stat['media'] = sum(lista_numero) / len(lista_numero)
    stat['varianza'] = sum(promedio_numero(lista_numero)) /len(lista_numero) - stat['media'] ** 2
    stat['deviacion_tipica'] = stat['varianza'] ** 0.5

    return stat


lista = [1,2,3,4,5]
print(estadistica(lista))

lista = [2.3, 5.7, 6.8 , 9.7 , 12.1, 15.6]
print(estadistica(lista))