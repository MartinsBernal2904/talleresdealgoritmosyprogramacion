#entradas
mujeres=int(input("Digite la cantidad de mujeres: "))
hombres=int(input("Digite la cantidad de hombres: "))
#caja negra
mp=(mujeres*100)/(mujeres+hombres)
hp=(hombres*100)/(mujeres+hombres)
#salidas
print(f"El porcentaje de mujeres es: {round (mp,2)} y el porcentaje de hombres es {round (hp,2)}")