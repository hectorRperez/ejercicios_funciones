""" Ejercicio 4
    
    Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
    La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
    y devolver el total de la factura. Si se invoca la función sin pasarle el 
    porcentaje de IVA, deberá aplicar un 21%. """

def agregar_iva(cobro_final, iva = 21):
    iva = iva / 100
    pago_final = iva * cobro_final
    cobro_final = cobro_final + pago_final

    return cobro_final

r = agregar_iva(1000,10)
print(r)