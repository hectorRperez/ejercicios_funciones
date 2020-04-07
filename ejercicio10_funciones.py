""" Ejercicio 10

    Escribir una función que convierta un número decimal en binario 
    y otra que convierta un número binario en decimal. """

def to_decimal(n):
    '''
    Función que transforma un número binario a decimal
    parametros:
        n: Es una cadena de 0 y 1 
    Devuelve:
        El numero decimal correspondiente a n
    '''

    n = list(n)
    n.reverse()
    decimal = 0

    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    
    return decimal


def to_binari(n):
    '''
    Función que transforma un número decimal a binario
    parametros:
        n: Es un numero entero 
    Devuelve:
        El numero binario correspondiente a n
    '''

    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2

    binario.reverse()
    return ''.join(binario)

print(to_decimal('10110'))
print(to_binari(22))