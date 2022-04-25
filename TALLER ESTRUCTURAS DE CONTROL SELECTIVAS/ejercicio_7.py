"""
entradas
distancia recorrida-->dr-->float
salida
precio que se debe pagar-->p-->
"""
#entrada
dr=float(input("Digite la distancia recorrida en km: "))
#salida
if(dr<=300):
    p=50000
    print("El precio que se debe pagar es: ",p)
elif(dr>300 and dr<1000):
    p=(70000+(dr-300)*30000)
    print("El precio que se debe pagar es: ",p)
elif(dr>300 and dr>1000):
    p=(150000+(dr-300)*9000)
    print("El precio que se debe pagar es: ",p)