"""
entradas
P-->p-->int
Q-->q-->int
salida
mensaje final-->mf-->
"""
#entrada
p=int(input("Digite el valor de p: "))
q=int(input("Digite el valor de q: "))
#salida
if(p**3+q**4-2*p**2>680):
    print(str(p)+" y "+ str(q)+" Si satisface la expresion ")
else:
    (p**3+q**4-2*p**2<680) 
    print(str(p)+" y "+ str(q)+" No satisface la expresion ")