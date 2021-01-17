
lista_precios=[0.33,1.07,1.43,2.46,3,4,5,6,7,9.2,9.45,9.85,10.8,11.8,12.9,13.95,15]

lista_rango_kw=[(0,100),(101,150),(151,200),(201,250),(251,300),(301,350),(351,400),(401,450),(451,500),(501,600),
				(601,700),(701,1000),(1001,1800),(1801,2600),(2601,3400),(3401,4200),(4201,5000)]

lista_precios_rangos=[(i[1]-i[0])*j for i,j in zip(lista_rango_kw,lista_precios)]

# print(lista_precios_rangos)

kw_consumidos=int(input('Teclee la cantidad de kw/h consumidos: '))

if kw_consumidos>0 and kw_consumidos<=5000:
	contador=0

	for i in lista_rango_kw:
		contador+=1

		if kw_consumidos<=i[1] and kw_consumidos>=i[0]:

			if contador==1:

				precio_pagar=kw_consumidos*0.33
				

			elif contador>1 and contador<18:

				precio_pagar=sum(lista_precios_rangos[:contador-1])+(kw_consumidos - lista_rango_kw[contador-2][1])*lista_precios[contador-1]
				

elif kw_consumidos>5000:
	precio_pagar=sum(lista_precios_rangos) + (kw_consumidos-5000)*20
	

print(f'Usted deberá pagar {precio_pagar:.2f} pesitos.')

	



