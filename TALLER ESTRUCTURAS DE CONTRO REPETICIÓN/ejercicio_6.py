#entrada 
c=int(0)
a=int(input("Ingrese el dividendo: "))
d=int(input("Ingrese el divisor: "))
#caja negra
a=a-d
#condicional
while(a>=0):
    c=c+1
    a=a-d
#salida
print("la división es igual a:"+str(c))