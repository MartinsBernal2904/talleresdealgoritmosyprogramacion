users = {
    "iperurena": {
    "nombre": "Iñaki",
    "apellido": "Perurena",
    "password": "123123"
    },
    "fmuguruza": {
    "nombre": "Fermín",
    "apellido": "Muguruza",
    "password": "654321"
    },
    "aolaizola": {
    "nombre": "Aimar",
    "apellido": "Olaizola",
    "password": "123456"
    }
    } 
a=0
def tryLogin():
    print("")
    usiario = input("Usuario: ")
    contraseña = str(input("Password: "))
    if(Usuario in users):
        if(users[Usuario]["password"]==contraseña):
            global userLogged
        userLogged=users[Usuario]
        return True
    return False
print("Pantalla de Login")
while(True):
    if(tryLogin()):
        print("Usuario logeado correctamente")
        print("Bienvenido, "+userLogged["nombre"]+" "+userLogged["apellido"])
    break
    a=a+1
    if(a>=3):
        print("")
    print("Itentos acabados")
    break
else:
        print("¡Credenciales incorrectas!")