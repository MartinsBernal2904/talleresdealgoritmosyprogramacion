estudiantes = {}
c=1
def getGrade():
    print("")
    nombre = str(input("Nombre: "))
    grado = int(input("Nota: "))
    estudiantes.update({nombre: grado})
def printGrades():
    print("")
    print(estudiantes)
while(True):
    print("")
    print("Datos del estudiante ",+str(c))
    getGrade()
    if(c>=3):
        break
    c=c+1
print(estudiantes)