""" Ejercicio 3

Escribir una función que reciba un número entero positivo y devuelva su factorial. """

def factorial_numero(numero):
    '''
    Funcion que calcula el factorial de un número entero positivo
    Parametros:
        recibe un número entero positivo
    Devuelve el factorial del número
    '''
    r = 1
    for i in range(1,numero+1):
        r = i * r
    
    return r


factorial = factorial_numero(7)
print('El factorial de {} '.format(factorial))
