"""
entradas
sueldo bruto-->sb-->int
salida
nuevo sueldo-->ns-->float
"""
#entradas
sb=int(input("Digite su sueldo bruto: "))
#caja negra 
if(sb<900000):
    ns=(sb*0.15)+sb
elif(sb>=900000):
    ns=(sb*0.12)+sb
#salidas 
print("Su sueldo final es: ", ns)