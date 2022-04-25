"""
entradas
cantidad dinero-->cd-->float
salida 
desglose-->d-->float
"""
#entradas
cd=int(input("Digite la cantidad de dinero: "))
a1=int(cd/100000)
a2=int((cd%100000)/50000)
a3=int(((cd%100000)%50000)/20000)
a4=int((((cd%100000)%50000)%20000)/10000)
a5=int(((((cd%100000)%50000)%20000)%10000)/5000)
a6=int((((((cd%100000)%50000)%20000)%10000)%5000)/2000)
a7=int(((((((cd%100000)%50000)%20000)%10000)%5000)%2000)/1000)
a8=int((((((((cd%100000)%50000)%20000)%10000)%5000)%2000)%1000)/500)
a9=int(((((((((cd%100000)%50000)%20000)%10000)%5000)%2000)%1000)%500)/200)
a10=int((((((((((cd%100000)%50000)%20000)%10000)%5000)%2000)%1000)%500)%200)/100)
a11=int(((((((((((cd%100000)%50000)%20000)%10000)%5000)%2000)%1000)%500)%200)%100)/50)
#salidas 
if a1>=1:
    print(a1,"Billetes de 100.000")
if a2>=1:
    print(a2,"Billetes de 50.000")
if a3>=1:
    print(a3,"Billetes de 20.000")
if a4>=1:
    print(a4,"Billetes de 10.000")
if a5>=1:
    print(a5,"Billetes de 5.000")
if a6>=1:
    print(a6,"Billetes de 2.000")
if a7>=1:
    print(a7,"Billetes de 1.000")
if a8>=1:
    print(a8,"Monedas de 500")
if a9>=1:
    print(a9,"Monedas de 200")
if a10>=1:
    print(a10,"Monedas de 100")
if a11>=1:
    print(a11,"Monedas de 50")
