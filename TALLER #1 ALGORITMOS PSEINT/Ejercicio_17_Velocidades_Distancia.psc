Algoritmo Ejercicio_17_Velocidades_Distancia
	Definir Velocidad_1, Velocidad_2, Distancia, Tiempo_minutos, t Como Real
	Escribir "Digite la velocidad del primer vehiculo en Km/h"
	Leer Velocidad_1
	Escribir "Digite la velocidad del segundo vehiculo en Km/h"
	Leer Velocidad_2
	Escribir "Digite la Distancia entre los dos vehiculos en Km"
	Leer Distancia
	si Velocidad_1>Velocidad_2 Entonces
		Tiempo_minutos<-Distancia/Velocidad_1
	SiNo
		Tiempo_minutos<-Distancia/Velocidad_2
		
	FinSi
	t<-Tiempo_minutos*60
	Escribir "El tiempo en minutos en que tarde en alcanzar al vehiculo es:" t
FinAlgoritmo
