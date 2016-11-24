#Aracely Velazquez Calderon
#Introduccion a la Programacion en python 2
#22/11/2016

def intereses(x):
    sum=0
    i=(x*0.04)
    sum=x+i
    return sum
x = input()
print intereses(x)

def intereses(x):
    sum=0
    i=(2*x*0.04)
    sum=x+i
    return sum
x = input()
print intereses(x)

def intereses(x):
    sum=0
    i=(3*x*0.04)
    sum=x+i
    return sum
x = input()
print intereses(x)


interes_por_year=0.04
saldo inicial=input("la cantidad a depositar")
nvo_saldo=0
for in range(4):
        saldo=saldo_inicial*1.04
    nvo_saldo=nvo_saldo+saldo
    print nvo_saldo
