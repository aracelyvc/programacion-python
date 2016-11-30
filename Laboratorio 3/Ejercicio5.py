#Aracely Velazquez Calderon
#Laboratorio 3
#29/11/2016
#Ejercicio 5

palabra=input("ingresa tu nombre entre comillas: ")
letra=palabra[0]

if letra == letra.lower():
    if letra in ("a","e","i","o","u"):
        print "La primera letra de su nombre es vocal"
    else:
        print "La primera letra de su nombre es consonante"
