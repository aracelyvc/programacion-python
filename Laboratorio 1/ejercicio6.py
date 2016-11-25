#Aracely Velazquez Calderon
#Introduccion a la Programacion en Python
#Laboratorio 1

print "ingresa tu peso(kg) y altura(m), ambos con punto decimal, por ejemplo: imc(50.0,1.60), depues de ello da enter y espera aque aparesca el reultado"
def imc(p,h):
    imc=p/(h*h)
    return imc
    print imc(p,h)
print"luego que haya aparecido el resultado ingresa tu imc con punto decimal, ejemplo: x(23.0) y da enter"

def x(imc):
    if imc < 16.0:
        print "delgadez severa"
    elif imc > 16.0 and imc < 16.99:
        print "delgadez moderada"
    elif imc > 17.0 and imc < 18.49:
        print "delgadez leve"
    elif imc > 18.5 and imc < 24.99:
        print "normal"
    elif imc <= 25:
        print "sobrepeso"
    elif imc <= 30:
        print "obesidad"
    elif imc <= 40:
        print "obesidad morbida"
