#entradas
Lectura_luz_mes_pas=float(input("Ingrese la cantiad de kilovatio del mes pasado: "))
Lectura_luz_mes_act=float(input("Ingrese la cantiad de kilovatio del mes actual: "))
Costo_kilo=float(input("Ingrese el costo de un kilovatio: "))
#caja negra
pago_mes_pas=Lectura_luz_mes_pas*Costo_kilo
pago_mes_act=Lectura_luz_mes_act*Costo_kilo
dif_meses=abs(pago_mes_act-pago_mes_pas)
#salidas
print("El valor de la factura del mes pasado es: ", pago_mes_pas)
print("El valor de la factura del mes actual es: ", pago_mes_act)
print("La diferencia en el valor de ambos meses es: ", dif_meses)