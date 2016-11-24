
print "ingresa tu peso(kg) y altura(m), ambos con punto decimal, por ejemplo: imc(50.0,160.0)"
def imc(p,h):
    imc=(p/(h*h))
    return imc
print imc

def clasificacion(imc):
    if imc<16.0:
        print "delgadez severa", calsificacion
    elif imc in range(16.0,16.99):
        print "delgadez moderada", clasificacion
    elif imc in range(17.0,18.49):
        print "delgadez leve", clasificacion
    elif imc in range(18.5,24.99):
        print "normal", clasificacion
    elif imc<=25:
        print "sobrepeso", clasificacion
    elif imc<=30:
        print "obesidad", clasificacion
    elif imc<=40:
        print "obesidad morbida", clasificacion
print clasificacion
