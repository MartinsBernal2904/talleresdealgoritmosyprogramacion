"""
entradas
reporte departamento #1-->a-->float
reporte departamento #2-->b-->float
reporte departamento #3-->c-->float
reporte de ventas total-->rvt-->float
porcentaje-->p-->float
salario-->s-->float
salida
salario neto final-->snf-->float
"""
#entradas
a=float(input("Digite el reporte del departamento #1: "))
b=float(input("Digite el reporte del departamento #2: "))
c=float(input("Digite el reporte del departamento #3: "))
s=float(input("Digite su salario: "))
#caja negra 
rvt=a+b+c
p=rvt*0.33
if(a>p):
    snf=(s*0.2)+s
#salida
print("El sueldo final de los trabajadores en cada departamento es de: ",snf)
