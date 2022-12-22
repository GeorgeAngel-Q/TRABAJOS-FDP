

# Ejercicio 12: Hallando el área de tres figuras geométricas

print ("Sistema para hallar el Área de una figura geométrica")
print("Bienvenido al sistema, puede encontrar el área del cuadrado,triángulo y rectangulo")
fig=input("Escriba el tipo de figura geométrica en minúscula:  ")

cua="cuadrado"
rec1="rectangulo"
rec2="rectángulo"
tri1="triángulo"
tri2="triangulo"

if fig == cua:
    print ("Área del cuadrado")
    lado = input("Coloque el lado del cuadrado:  ")
    lado = float(lado)
    Acua=lado**2
    print ("El área del cuadrado es ",Acua)
    
elif fig==tri1 or fig==tri2:
    print ("Área del triángulo")
    base = float(input("Coloque la base de su triangulo (u):  "))
    altu = float(input("Coloque la altura de su triangulo (u):  "))
    Atri= (base * altu) /2
    print ("El área del triángulo es ",Atri)

elif fig==rec1 or fig==rec2:
    print ("Área del rectángulo")
    base= float(input("Coloque la base del rectángulo (u):  "))
    altu= float(input("Coloque la altura del rectángulo(u):  "))
    Arec=base*altu
    print ("El Área del rectangulo es ",Arec)


else:
    print ("Verifique que el nombre de la figura este correctamente escrita")