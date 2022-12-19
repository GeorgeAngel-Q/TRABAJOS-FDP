if __name__ == '__main__':
	print("Sistema de pedidos del restaurante")
  #Deberá elegir el número de platos de cada opción
	suma = int()
	m = int()
	n = int()
	p = int()
	cevichedeconchasnegras = 42
	cevichedepescadoalacrema = 39
	chicharrondecalamar = 43
	acumula = 0
	m = 0
	n = 0
	r = 0
	z = 1
	if z==1:
		print("Seleccione una opcion")
		print("1. Ceviche de conchas negras = 42 soles")
		print("2. Ceviche de Pescado a la crema= 39 soles")
		print("3. Chicharron de calamar =43 soles")
		pl = float(input())
		if pl==1:
			print("Ha elegido Ceviche de conchas negras")
			print("Ingrese cantidad de platos")
			m = int(input())
			acumula = acumula+cevichedeconchasnegras*m
      
		elif pl==2:
			print("Ha elegido Ceviche de Pescado a la crema")
			print("Ingrese cantidad de platos")
			n = int(input())
			acumula = acumula+cevichedepescadoalacrema*n
      
		elif pl==3:
			print("Ha elegido Chicharron de calamar")
			print("Ingrese cantidad de platos")
			r = float(input())
			acumula = acumula+chicharrondecalamar*r
			
		else:
			print("Opcion no valida, ingrese otro numero")

	if z==1:
		print("Seleccione una opcion")
		print("1. Ceviche de conchas negras = 42 soles")
		print("2. Ceviche de Pescado a la crema= 39 soles")
		print("3. Chicharron de calamar =43 soles") 
		pl = float(input())
		if pl==1:
			print("Ha elegido Ceviche de conchas negras")
			print("Ingrese cantidad de platos")
			m = int(input())
			acumula = acumula+cevichedeconchasnegras*m
      
		elif pl==2:
			print("Ha elegido Ceviche de Pescado a la crema")
			print("Ingrese cantidad de platos")
			n = int(input())
			acumula = acumula+cevichedepescadoalacrema*n
      
		elif pl==3:
			print("Ha elegido Chicharron de calamar")
			print("Ingrese cantidad de platos")
			r = float(input())
			acumula = acumula+chicharrondecalamar*r

	if z==1:
		print("Seleccione una opcion")
		print("1. Ceviche de conchas negras = 42 soles")
		print("2. Ceviche de Pescado a la crema= 39 soles")
		print("3. Chicharron de calamar =43 soles") 
		pl = float(input())
		if pl==1:
			print("Ha elegido Ceviche de conchas negras")
			print("Ingrese cantidad de platos")
			m = int(input())
			acumula = acumula+cevichedeconchasnegras*m
      
		elif pl==2:
			print("Ha elegido Ceviche de Pescado a la crema")
			print("Ingrese cantidad de platos")
			n = int(input())
			acumula = acumula+cevichedepescadoalacrema*n
      
		elif pl==3:
			print("Ha elegido Chicharron de calamar")
			print("Ingrese cantidad de platos")
			r = float(input())
			acumula = acumula+chicharrondecalamar*r
		print("Para salir de escriba: 2")
		z = float(input())
	print("La cuenta total es : ",acumula)