#entradas
x=float(input("Ingrese el valor x de naranjas: "))
y=float(input("Ingrese el valor y de docena: "))
k=float(input("Ingrese el valor k de ganacias: "))
#caja negra 
porcen_ganacia=abs(((x*y)/k)*0.1)
#salidas
print("El porcentaje de ganacias obtenidas es: ",round(porcen_ganacia,2),"%")