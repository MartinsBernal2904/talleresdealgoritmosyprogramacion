"""
entradas
a-->int
b-->int
c-->int
d-->int
salida 
respuesta#1-->res1-->float
respuesta#2-->res2-->float
"""
#entradas
a=int(input("Digite un numero entero: "))
b=int(input("Digite un numero entero: "))
c=int(input("Digite un numero entero: "))
d=int(input("Digite un numero entero positivo: "))
#caja negra 
if(d==0):
    res1=(a-c)**2
    res2=(((a-b)**3)/d)
elif(d>0):
    res1=(a-c)**2
    res2=(((a-b)**3)/d)
#salidas
print("El resultado # 1 es: ",res1)
print("El resultado # 2 es: ",res2)