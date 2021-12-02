#Librerías
import numpy as np
from random import random, randint
from math import log10, fmod
from decimal import Decimal


#Definición de parametros
DIFS = 10e-3
SIFS = 5e-3
durRTS = 11e-3
durCTS = 11e-3
durACK = 11e-3
durDATA = 43e-3
sigma = 1e-3 #Duración de cada miniranura
H = 7 #Número de nodos
K = 15 #Tamaño del buffer
E = 18 #sleep factor
N = [5,10,15,20] #Número de nodos por grado
n = 1 #Indice de nodos
W = [16,32,64,128,256] #Miniranuras
w = 1 #Indice de miniranuras
landa = [0.0005,0.001,0.005,0.03] #Tasa de generación de paquetes
l = 0 #Indice de landa

#Tiempo de slot
Tslot = sigma*W[w] + DIFS + 3*SIFS + durRTS + durCTS + durDATA + durACK 

#Ciclo de trabajo
Tcycle = (E + 2) * Tslot

#Matriz del sistema
Nodos = np.zeros((N[n],H))

collisions = np.zeros((1, 7))
fullbuffer = np.zeros((1, 7))
nodeTimes = np.zeros((1, 7))
countersuccess = np.zeros((1, 7))
counterontransit = np.zeros((1, 7))
piepackages = np.zeros((1, 3))
transpergrade = np.zeros((1, 7))

hashMap = {}

for k in range(0,N[n]):
    for v in range(0,H):
        hashMap["{}{}".format(k,v)] = np.zeros((1,K))
       
    
#Garantiza que hay almenos un arribo al inicar la simulacion 
ta = -1
pg = 0
tsim = 0
final = 0
counter = 0

Pa = np.zeros((1,5))
contendientes = np.zeros((1, N[n]))
numPaquete = 0

#Generacion de paquetes
for i in range (1,1330000+1):
    if(ta <= tsim):
        landa2 = landa[l]*N[n]*H
        U = (1e6*random())/1e6
        nuevot = -(1/landa2)*log10(1-U)
        nodo = randint(0,N[n]-1)
        grado = randint(0,H-1)

        if(Nodos[nodo,grado] < 15):
            Nodos[nodo,grado] = Nodos[nodo,grado] + 1
            llave = str(nodo) + str(grado)
            aux = hashMap[llave]
            index = np.where(aux == 0)[1]
                    
            if(index.size != 0):
                pg = pg + 1
                aux[0][index[0]] = pg
                hashMap[llave] = aux
                aux = 0                  

            Pa[pg-1][0] = pg
            Pa[pg-1][1] = nodo
            Pa[pg-1][2] = grado
            Pa[pg-1][3] = ta
            Pa = np.vstack([Pa,np.zeros((1,5))])  
    
    ta = tsim + nuevot

    if(round(Decimal(str(i))%Decimal(str(Tcycle))) == 0):
        #Transmisión, recorremos desde nodo más alejado
        for grado in range(H-1,0):
            for fila in range(0,N[n]):
                if(Nodos[fila,grado] != 0):
                    contendientes[0][fila] = randint(0,W[n])
                else:
                    contendientes[0][fila] = None

                