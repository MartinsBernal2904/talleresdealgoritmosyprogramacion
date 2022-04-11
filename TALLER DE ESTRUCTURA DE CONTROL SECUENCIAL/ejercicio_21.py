#entradas
p=float(input("Ingrese e valor de contando de la compra: "))
t=float(input("Ingrese el valor de la compra a 12 cuotas: "))
#caja negra
dife=(t-p)
porcen_dife=abs(((p-dife)/100)*0.001)
porcen_recargo=1-porcen_dife
#salidas
print("El porcentaje de recargo por la compra a cuotas es: ", round(porcen_recargo,2))