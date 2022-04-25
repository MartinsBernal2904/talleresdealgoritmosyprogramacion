"""
entradas
monto compra-->mc-->float
nombre cliente-->nc-->str
salida
nombre cliente-->nc-->str
monto compra-->mc-->float
monto a pagar-->mp-->float
descuento-->d-->float 
"""
#entradas
nc=str(input("Digite el nombre de cliente: "))
mc=float(input("Digite el monto de la compra: "))
#salida
if(mc<50000):
    d=0
    mp=mc
    print("nombre del cliente: ",nc)
    print("monto de la compra: ",mc)
    print("monto a pagar: ",mp)
    print("descuento recibido: ",d)
elif(mc>50000 and mc<=100000):
    d=mc*0.05
    mp=mc-d
    print("nombre del cliente: $",nc)
    print("monto de la compra: $",mc)
    print("monto a pagar: $",mp)
    print("descuento recibido: $",d)
elif(mc>100000 and mc<=700000):
    d=mc*0.11
    mp=mc-d
    print("nombre del cliente: $",nc)
    print("monto de la compra: $",mc)
    print("monto a pagar: $",mp)
    print("descuento recibido: $",d)
elif(mc>700000 and mc<=1500000):
    d=mc*0.18
    mp=mc-d
    print("nombre del cliente: $",nc)
    print("monto de la compra: $",mc)
    print("monto a pagar: $",mp)
    print("descuento recibido: $",d)
elif(mc>1500000):
    d=mc*0.25
    mp=mc-d
    print("nombre del cliente: $",nc)
    print("monto de la compra: $",mc)
    print("monto a pagar: $",mp)
    print("descuento recibido: $",d)