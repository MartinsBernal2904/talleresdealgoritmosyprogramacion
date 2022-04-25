"""
entradas
numero #1-->a-->int
numero #2-->b-->int
numero #3-->c-->int
numero #4-->d-->int
numero final-->n-->int
salida
redondeo-->re-->int
"""
#entradas
a= (input("Digite el numero #1: "))
b= (input("Digite el numero #2: "))
c= (input("Digite el numero #3: "))
d= (input("Digite el numero #4: "))
#caja negra
n=int((a+b+c+d))
#salida
c=int(c)
if(c>5):
    re=round(n, -2)
    print(re)
else:
    (c<5)
    r=int((round(n, -2)))
    print(re)