"""
entradas
categoria-->c-->int
sueldo bruto-->sb-->float
salida
aumento-->a-->float
nuevo sueldo-->ns-->float
"""
#entrada
sb=float(input("Digite el salario bruto: "))
#salidas
if(sb==5000000):
    a=sb*0.1
    ns=sb+a
    print("La categoria #1 y su nuevo salario es de:  $",ns)
elif(sb==4300000):
    a=sb*0.15
    ns=sb+a
    print("La categoria #2 y su nuevo salario es de:  $",ns)
elif(sb==3600000):
    a=sb*0.2
    ns=sb+a
    print("La categoria #3 y su nuevo salario es de:  $",ns)
elif(sb==2000000):
    a=sb*0.4
    ns=sb+a
    print("La categoria #4 y su nuevo salario es de:  $",ns)
elif(sb==900000):
    a=sb*0.6
    ns=sb+a
    print("La categoria #5 y su nuevo salario es de:  $",ns)

