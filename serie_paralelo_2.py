# Solucionar un circuito serie o paralelo de N resistencias
# Yerman Avila

# Variables
    #Entrada
Vcc=float(input("Ingrese el valor de Vcc= "))
R=[]
tipo_circuito=input("Tipo de circuito S para serie P para paralelo: ")

    #Salida
IT=0.0
RT=0.0
I=[]
P=[]
Vserie=[]

print("Ingrese la Resistencia, finalice con *: ")

while True:
    dato=input()
    if(dato=="*"):
        break
    R.append(float(dato))

if(tipo_circuito=="S"):
    print("Eligió circuito Serie ... \n")
    RT=sum(R)
    IT=Vcc/RT

    for i in range(len(R)):
        voltaje=IT*R[i]
        Vserie.append(voltaje)
        P.append(voltaje*IT)
    
    PT=Vcc*IT
    
    print("Resistencias ingresadas: ", R, " En [Ohm]")
    print("Voltajes de cada resistencia: ", Vserie, " En [V]")
    print("Potencias calculadas: ", P, "En [W]")

elif(tipo_circuito=="P"):
    print("Eligió circuito Paralelo ... \n")

    print("Resistencias ingresadas: ", R)
    print("Potencias calculadas: ", P)
else:
    print("Error...")


print("Resistencia Total: ", RT)
print("Potencia Total: ", PT)

print(IT)