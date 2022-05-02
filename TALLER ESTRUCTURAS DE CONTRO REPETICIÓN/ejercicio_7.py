while True:
    #entradas
    datos=input()
    x,m=datos.split(" ")
    x=int(x)
    m=int(m)
    #condicional
    if(x==0 and m==0):
        break
    #caja negra
    r=x*m
    #salida
    print(r)
