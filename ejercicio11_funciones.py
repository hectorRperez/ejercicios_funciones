""" Ejercicio 11

    Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario 
    con cada palabra que contiene y 
    su frecuencia. Escribir otra función que reciba el diccionario 
    generado con la función anterior y devuelva una 
    tupla con la palabra más repetida y su frecuencia. """



def contar_palabras(palabra):
    '''
    Función que cuenta el número de veces que una palabra esta en una cadena de caracteres
    parametro:
        palabra = una cadena de texto con palabra
    Devuelve:
        Un diccionario con palabras y el número de veces que está en una cadena
    '''
    palabra = palabra.split(' ')
    mi_diccionario = {}

    for i in palabra:
        if i in mi_diccionario:
            mi_diccionario[i]+=1
        else:
            mi_diccionario[i] = 1

    return mi_diccionario

def palabra_mas_repetida(palabra):
    '''
    Función que busca las palabras que más se repiten en un diccionario de palabras
    parametros:
        palabra = un diccionario {palabra:frecuencia}
    Devuelve
        Una lista con la palabra que más se repite en el diccionario palabra
    '''
    max_palabra = ''
    max_frecuencia = 0

    for key,value in palabra.items():
        if value > max_frecuencia:
            max_palabra = key
            max_frecuencia = value

    return max_palabra, max_frecuencia

palabra = input('Ingrese una palabra: ')
print(contar_palabras(palabra))
print(palabra_mas_repetida(contar_palabras(palabra)))
