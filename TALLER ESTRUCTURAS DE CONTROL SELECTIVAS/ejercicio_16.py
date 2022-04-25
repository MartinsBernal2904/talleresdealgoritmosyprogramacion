"""
entradas
A-->a-->float
B-->b-->float
c-->c-->float
salidas
X1-->x1-->float
X2-->x2-->float
"""
#entrada
from math import sqrt
a=float(input("A: "))
b=float(input("B: "))
c=float(input("C: "))
#caja negra
d=b**2-(4*a*c)
X1=0.0
x2=0.0
#salidas
if d==0:
    x1=x2=b/(2*a)
    print("x1: ",x1)
    print("x2: ",x2)
elif(d>0):
    x1=(-b+sqrt(b**2-4*a*c)/(2*a))
    x2=(-b-sqrt(b**2-4*a*c)/(2*a))
    print("x1: ",x1)
    print("x2: ",x2)
else:
    print("No tiene solución en bases reales")