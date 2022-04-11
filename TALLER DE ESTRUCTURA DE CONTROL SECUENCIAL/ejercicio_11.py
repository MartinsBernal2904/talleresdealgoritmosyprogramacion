#entradas
nombre=str(input("Ingrese su nombre: "))
numero_horas=int(input("Ingrese las horas que trabajo: "))
pago_horas=float(input("Ingrese el valor pagado por hora: "))
horas_extra=int(input("Ingrese las horas extra: "))
numero_hijos=int(input("Ingrese cuantos hijos tiene: "))
#caja negra
sueldo_base=(numero_horas*pago_horas)+(horas_extra*pago_horas*0.25)
deduccion=sueldo_base*0.14
asignaciones=250000+173000*numero_hijos+180000
Sueldo_total=sueldo_base+asignaciones-deduccion
#salidas
print("El sueldo base del trabajor es: ", sueldo_base)
print("Las deducciones al sueldo base son: ", round(deduccion,2))
print("Las asignaciones al sueldo base son: ", asignaciones)
print(nombre,"EL sueldo neto para diciembre es: ", Sueldo_total)