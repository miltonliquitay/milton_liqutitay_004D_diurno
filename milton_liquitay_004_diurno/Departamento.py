import os
import numpy as np
def llenar(departamento,depas):
    p=1
    for i in range(10):
        for j in range(4):
            departamento[i,j]=p
            p+=1
def valiaop():
    op=0
    while(True):
        try:
            op=int(input(" Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print(" Error, Debe ingresar una opcion entre 1 y 5")
        except ValueError:
            print("Solo debe ingresar un numero entero positivo!")
    return op
def valiatipo(departamento):
    os.system("cls")
    tipo=""
    while(len(tipo)<=0):
        print()
        print("Seleccione el tipo A/B/C/D")
        tipo=input(" Elija un tipo: ").lower()
        if(tipo!="a" and tipo!="b" and tipo!="c" and tipo!="d"):
            print("Error, debe ingresar un tipo valido")
            tipo=""
    return tipo
def dpto(departamento,tipo):
    dpto=0
    while(True):
        try:
            dpto=int(input(" Ingrese un piso que quiera comprar entre 1 y 40 "))
            if(dpto>=1 and dpto<=10):
                break
            else:
                print("Debe ingresar una opción valida")
        except ValueError:
            print(" Debe ingresar un numero entero")
    return dpto
def dptodis(departamento,dpto):
    for i in range(10):
        for j in range(4):
            if(dpto==departamento[i,j]):
                return True
    return False
def comprardpto(departamento,tipo,dpto,depas,ruts):
    if(tipo=="a"):
        pago=3800
    if(tipo=="b"):
        pago=3000
    if(tipo=="c"):
        pago=2800
    if(tipo=="d"):
        pago=3500
    for i in range(10):
        for j in range(4):
            if(dpto==departamento[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input(" Ingrese su RUN "))
                            if(rut<99999999):
                                print(" Error, el run debe tener minimo 9 digitos ")
                            else:
                                break
                        except ValueError:
                            print("Debe ser numeros enteros")
                    if(len(ruts)>0):
                        sw=0
                        for y in range(len(ruts)):
                            if(rut==ruts[y]):
                                sw=1
                        if(sw==1):
                            print("El rut ya esta registrado ")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break           

    return pago
def mostrardpto(depa):
    depa[depa==dpto]="x"
    asd=np.empty([10,4],type(int))
    dis=1
    for i in range(10):
        for j in range(4):
            asd[i,j]=dis
            dis+=1
def listcom(rut):
    rut.sort()
    print(" El listado de compradores de menor a mayor es: ")
    print("\t",rut)
def totalr(depa):
    suma=0
    for i in range(10):
        for j in range(4):
            if(depa[i,j]!=0 and depa[i,j]>40):
                suma+=depa[i,j]
    return suma

