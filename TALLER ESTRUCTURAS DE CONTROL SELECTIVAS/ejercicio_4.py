"""
entradas
monto compra-->mc-->float
salida
fondos empresa-->fe-->float
pago a credito-->pc-->float
pago de intereses-->pi-->float
prestamo banco-->pb-->float
"""
#entradas
mc=float(input("Digite el monto de la compra: "))
#caja negra}
if(mc>5000000):
    fe=mc*0.55
    pc=mc*0.15
    pi=(pc*0.2)+pc
    pb=mc*0.3
elif(mc<=5000000):
    fe=mc*0.7
    pc=mc*0.3
    pi=(pc*0.2)+pc
    pb="No lo necesita"
#salidas
print("La inversion por fondos de la empresa es: ",fe)
print("El valor a pagar del credito es: ",pc)
print("El valor a pagar por intereses es:",pi)
print("El valor prestado por el banco es de: ",pb)

