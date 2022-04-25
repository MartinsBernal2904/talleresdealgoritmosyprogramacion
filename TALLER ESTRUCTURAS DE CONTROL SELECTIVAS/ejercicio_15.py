"""
entradas
nivel hemoglobina-->nh-->float
edad-->e-->int
sexo-->s-->str
salida
resultado anemia-->a-->str
"""
#entradas
e=int(input("Ingrese edad del paciente en meses: "))
s=input("Ingrese el sexo del paciente: ")
nh=float(input("Ingrese nivel de hemoglobina del paciente: "))
#caja negra 
a=e/12
#salidas
if e>=0 and e<=1:
    if nh<13:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if e>1 and e<=6:
    if nh<10:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if e>6 and e<=12:
    if nh<11:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if a>1 and a<=5:
    if nh<11.5:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if a>5 and a<=10:
    if nh<12.6:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if a>10 and a<=15:
    if nh<13:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if s=="mujer" and a>15:
    if nh<12:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")
if s=="hombre" and a>15:
    if nh<14:
        print("El resultado del paciente es positivo. Tiene Anemia")
    else:
        print("El resultado del paciente es negativo. No tiene Anemia")

