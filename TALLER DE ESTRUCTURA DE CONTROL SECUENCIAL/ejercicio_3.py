#Entradas
sueldo_base=int(input("Ingrese su sueldo base: "))
venta1=int(input("Ingrese el valor de la venta 1: "))
venta2=int(input("Ingrese el valor de la venta 2: "))
venta3=int(input("Ingrese el valor de la venta 3: "))
#caja negra
total_ventas=venta1+venta2+venta3
comision=total_ventas*0.10
pago_total=sueldo_base+comision
#salidas
print(f"su comision es {round (comision,0)} y el total a pagar es {round (pago_total,0)}")
