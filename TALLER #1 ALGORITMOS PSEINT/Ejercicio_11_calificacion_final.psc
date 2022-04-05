Algoritmo Ejercicio_11_calificacion_final
	Definir a, b, c, examen, trabajo Como Real
	Escribir "Digite la nota de su primer parcial"
	Leer a
	Escribir "Digite la nota de su segundo parcial"
	Leer b
	Escribir "Digite la nota de su tercer parcial"
	Leer c
	Escribir "Digite la nota de su examen final"
	Leer examen
	Escribir "Digite la nota de su trabajo final"
	Leer trabajo
	notas_parciales<-(a+b+c)/3
	prom<-notas_parciales*0.55
    Promedio_examen<-examen*0.30
	promedio_trabajo<-trabajo*0.15
	Nota_final<-prom+Promedio_examen+promedio_trabajo
	Escribir "su Nota final de algoritmos es:" Nota_final
FinAlgoritmo
