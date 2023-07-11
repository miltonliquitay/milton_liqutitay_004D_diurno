import os
import numpy as np 
import Departamento as fa
departamento=np.empty([10,4],type(int))
depas=np.empty([10,4],type(int))
ruts=[]
fa.llenar(departamento,depas)
op=0
depas=0
suma=0

while(op!=5):
    os.system("cls")
    print("     Casa Feliz      ")
    print("     **********************     ")
    print(" 1. =>  comprar departamento ")
    print(" 2. =>  Mostrar departamentos disponibles ")
    print(" 3. =>  Ver listado de compradores ")
    print(" 4. =>  Mostrar ganancias totales ")
    print(" 5. =>  salir ")
    op=fa.valiaop()
    if(op==1):
        print(departamento)
        os.system("pause")
        fa.valiatipo(departamento)
        tipo=fa.valiatipo(departamento)
        fa.dpto(departamento,tipo)
        dpto=fa.dpto(departamento,tipo)
        dd=fa.dptodis(departamento,dpto)
        if(dd):
            print(" Departamento Disponible: ", tipo,dpto)
            pagar=fa.comprardpto(departamento,tipo,dpto,depas,ruts)
            print(" Usted debera pagar un total de : UF,", pagar)
            input("<<Enter>> para continuar")
            print(" !La operacion se ha realizado con gusto ")
            os.system("pause")

    if(op==2):
        print(departamento)
        os.system("pause")
    if(op==3):
        fa.listcom(ruts)
        os.system("pause")
    if(op==4):
        suma=0
        suma=fa.totalr(departamento)
        if(suma==0):
            print(" No se han realizado ventas ")
            os.system("pause")
        else:
            print(" El total vendido es de : UF,", suma)
    if(op==5):
        print("¡¡Gracias por comprar y tenga buen dia!! , Milton Liquitay 11/7/2023")
