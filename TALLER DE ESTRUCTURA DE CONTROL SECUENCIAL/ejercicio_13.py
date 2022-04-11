#entradas
N1=int(input("Ingrese cuantos billetes de 50 mil hay: "))
N2=int(input("Ingrese cuantos billetes de 20 mil hay: "))
N3=int(input("Ingrese cuantos billetes de 10 mil hay: "))
N4=int(input("Ingrese cuantos billetes de 5 mil hay: "))
N5=int(input("Ingrese cuantos billetes de 2 mil hay: "))
N6=int(input("Ingrese cuantos billetes de 1 mil hay: "))
N7=int(input("Ingrese cuantos billetes de 500 hay: "))
N8=int(input("Ingrese cuantos billetes de 100 hay: "))
#caja negra
Bill_50_mil=N1*50000
Bill_20_mil=N2*20000
Bill_10_mil=N3*10000
Bill_5_mil=N4*5000
Bill_2_mil=N5*2000
Bill_1_mil=N6*1000
Bill_500=N7*500
Bill_100=N8*100
Dinero_total=Bill_50_mil+Bill_20_mil+Bill_10_mil+Bill_5_mil+Bill_2_mil+Bill_1_mil+Bill_500+Bill_100
#salida
print("El dinero total que posee el banco es: ", Dinero_total )