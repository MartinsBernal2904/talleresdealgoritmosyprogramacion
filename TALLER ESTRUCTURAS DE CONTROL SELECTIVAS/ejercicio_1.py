"""
entrada
capital-->ca-->float
porcentaje interes-->pin-->float
salida
dinero obtenido-->di-->float
dinero total-->dt-->float
"""
#entradas
ca=float(input("Digite el capital que invirtio: "))
pin=float(input("digite el porcentaje de interes: "))
#caja negra 
di=ca*pin
intereses=""
if(di>100000):
    intereses="debe reinvertir"
elif(di<=100000):
    intereses="no debe reinvertir"
dt=ca+di
#salidas
print("El dinero total por los intereses es: ", di)
print(f"{intereses}")