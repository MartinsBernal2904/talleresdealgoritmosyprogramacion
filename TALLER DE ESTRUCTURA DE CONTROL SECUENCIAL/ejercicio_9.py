#entradas
pago_hora=int(input("Ingrese el valor pago por hora: "))
horas=int(input("Ingrese las horas que trabajo: "))
#caja negra
sueldo=pago_hora*horas
descuento=sueldo*0.20
sueldo_neto=sueldo-descuento
#salida
print("su sueldo neto con el descuento es de: ",sueldo_neto)