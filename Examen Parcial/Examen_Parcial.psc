Algoritmo Examen_Parcial
	Escribir "Bienvenida"
	desacierto=2
	acierto=3
	win=0
	lose=0
	resp="si"
	quest="si"
	saldo=10
	Escribir "�Desea apostar?"
	Leer resp
	Mientras resp="si"y quest="si" y saldo>2 Hacer
		x=1
		z=2
		c=Per�
		d=Chile
		Mostrar "El partido se llevar� a cabo entre Per� y Chile"
		Escribir "Ingrese los goles a favor de Per�: "
		Leer marc1
		Escribir "Ingrese los goles a favor de Chile: "
		Leer marc2
		Si marc1=x y marc2=z Entonces
			Escribir "Felicidades usted acert�"
			saldo=saldo+acierto
			win<-win+1
			Mostrar "saldo actual: ",saldo
			Escribir "�Desea volver jugar?"
			Leer quest
		Sino
			Escribir "Usted perdi�"
			saldo=saldo-desacierto
			lose<-lose+1
			Mostrar "saldo actual: ",saldo
			Escribir "�Desea volver jugar?"
			Leer quest
		FinSi
	Fin Mientras
	Mostrar "Numero de aciertos: ",win
	Mostrar "N�mero de desaciertos: ",lose
	Mostrar "Saldo final: ",saldo
FinAlgoritmo
