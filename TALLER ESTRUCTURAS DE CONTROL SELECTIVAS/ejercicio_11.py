"""
Entradas
temperatura en grados fahrenheit-->float-->t
Salidas
deporte-->str-->d
"""
#Entradas
t=float(input("Digite temperaturas: "))
#caja negra
d=""
if(t>85 and t<=120):
    d="Natacion"
elif(t>70 and t<=85):
    d="Tenis"
elif(t>32 and t<=70):
    d="Golf"
elif(t>10 and t<=32):
    d="Esqui"
elif(t>=0 and t<=10):
    d="Marcha"
else:
    d="La temparatura no pertenece a ningun deporte"
#salida
print(f"El deporte a practicar es: {d}")