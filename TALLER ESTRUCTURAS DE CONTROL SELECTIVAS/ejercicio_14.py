"""
entradas
lectura anterior-->l1-->float
lectura actual-->l2-->float
salidas
costo factura-->cf-->float
"""
#entradas
l1=float(input("Ingrese la lectura anterior: "))
l2=float(input("Ingrese la lectura actual: "))
#caja negra
kw=l1-l2
#salidas
if kw>=0 and kw<=100:
    cf=4600
    print("El costo de la factura es de: ",(kw*cf)," COP")
if kw>100 and kw<=300:
    cf=80000
    print("El costo de la factura es de: ",(kw*cf)," COP")
if kw>300 and kw<=500:
    cf=100000
    print("El costo de la factura es de: ",(kw*cf)," COP")
if kw>500:
    cf=120000
    print("El costo de la factura es de: ",(kw*cf)," COP")