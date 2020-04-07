""" Ejercicio 7

    Escribir una función que reciba una muestra de números en una lista 
    y devuelva otra lista con sus cuadrados. """

def cuadrado_numero(lista_numero):
    '''
    Función que calcula los cuadrados de una lista de números
    parametros: 
        lista_numero es una lista de numeros
    Devuelve:
        Una lista con el cuadrado de los números que recibio en la lista
    '''
    lista_cuadrado = []

    for i in lista_numero:
        cuadrado = i ** 2

        lista_cuadrado.append(cuadrado)

    return lista_cuadrado


lista_numero = [10,244,32,478,54514]

r = cuadrado_numero(lista_numero)
print(r)


