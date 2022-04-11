#entradas
parcial1=int(input("Ingrese la nota de su primer parcial: "))
parcial2=int(input("Ingrese la nota de su segundo parcial: "))
parcial3=int(input("Ingrese la nota de su tercer parcial: "))
examen=int(input("Ingrese la nora de su examen final: "))
trabajo=int(input("Ingrese la nota de su trabajo final: "))
#caja negra
notas_parciales=(parcial1+parcial2+parcial3)/3
prom_parciales=notas_parciales*0.55
prom_examen=examen*0.30
prom_trabajo=trabajo*0.15
nota_final=prom_parciales+prom_examen+prom_trabajo
#salidas
print("Su nota final de algoritmos es: ",nota_final)