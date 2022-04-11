#entradas
valor_prestamo=float(input("Ingrese el valor del prestamo en Bolivares: "))
pago_intereses=float(input("Ingrese el valor de los intereses pagados en Bolivares: "))
#caja negra
razon=((pago_intereses*100)/(valor_prestamo*4))
print("El porcentaje anual cobrado por el prestamo es: ", razon)