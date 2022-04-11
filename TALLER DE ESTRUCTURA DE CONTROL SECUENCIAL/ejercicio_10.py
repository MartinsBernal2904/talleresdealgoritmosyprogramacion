#entradas
chelines=float(input("Ingrese cantidad de chelines austriacos: "))
dracmas=float(input("Ingrese cantidad de dracmas griegos: "))
pesetas=float(input("Ingrese cantidad de pesetas: "))
#caja negra
che_pes=chelines*(956.871/100)
drac_fra_f=dracmas*(88.607/100)*(1/20.110)
pes_dolar=pesetas*(1/122.499)
pes_liras_ita=pesetas*(100/9.289)
#salida
print(chelines, "chelines equivalen a: ", round(che_pes,2), "pesetas")
print(dracmas, "dracmas griegos equivalen a: ", round(drac_fra_f,2), "francos franceses")
print(pesetas, "pesetas equivalen a: ", round(pes_dolar,2), "dolares")
print(pesetas, "pesetas equivalen a: ", round(pes_liras_ita,2), "liras italianas")
