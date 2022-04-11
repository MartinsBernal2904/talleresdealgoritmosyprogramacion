#entradas
precio_final=float(input("Ingrese el precio final de la compra: "))
precio_venta=float(input("Ingrese el precio de venta de la compra: "))
#caja negra
descuento=abs(((precio_final-precio_venta)/100)*0.01)
valor_compra=precio_final-descuento
#salidas
print("El descuento aplicado a la compra es: ", descuento)
print("El valor real de la compra es: ", valor_compra)