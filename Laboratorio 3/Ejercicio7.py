#Aracely Velazquez Calderon
#Laboratorio 3
#29/11/2016
#Ejercicio 7

a=input("ingresa un nombre: ")
nombre=[a]
b=[a]
del(nombre[0])
if nombre[0] in ("a","e","i","o","u"):
    nombre=nombre
else:
    del(nombre[0])

print b,"!", b, b, "bo B",nombre, "Bonana fanna fo F",nombre, "Fee fy mo M",nombre, b"!"
