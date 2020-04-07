""" Ejercicio 6

    Escribir una función que reciba una muestra de números en una lista y devuelva su media. """


def media(lista_numero):

    contador = 0
    for i in lista_numero:
        contador += i
    
    return contador / len(lista_numero)

lista_numero = [1,2,3,4,12,30,45]

resultado_promedio = media(lista_numero)
print(resultado_promedio)