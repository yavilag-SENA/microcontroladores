#Circuito Serie o Paralelo
# Autor: Yerman Avila

#Variables de entrada
Vcc=0.0      #Voltaje de entrada
R=[]
tipo_circ=input("Tipo circuito (S) para serie o (P) paralelo \n")

#Variables de salida
RT=0.0
IT=0.0
    #Serie
Voltajes=[]
    #Paralelo
Corrientes=[]

if(tipo_circ=="S"):
    print("Circuito elegido: Serie \n")
    Vcc=float(input("Voltaje de alimentación: "))

    while True:
        dato=input("Valor de resistencia, finalice con * \n")
        if(dato=="*"):
            break
        else: 
            dato=int(dato)
            R.append(dato)

    #print(R)

    RT=sum(R)
    IT=Vcc/RT
    print("RT= ", RT, " [Ohm]")
    print("IT= ", IT, " [A]")

    for i in range(len(R)):
        aux=IT*R[i]
        Voltajes.append(aux)

    print("Voltajes en cada R son: ", Voltajes)


elif(tipo_circ=="P"):
    print("Circuito elegido: Paralelo \n")

    
else:
    print("Error Hasta luego....")


