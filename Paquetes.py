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
l = 0#Indice de landa

#Tiempo de slot
Tslot = sigma*W[w] + DIFS + 3*SIFS + durRTS + durCTS + durDATA + durACK 

#Ciclo de trabajo
Tcycle = (E + 2) * Tslot

#Matriz del sistema
Nodos = np.zeros((N[n],H))

collisions = [0] * 7
fullbuffer = [0] * 7
nodeTimes = [0] * 7
countersuccess = [0] * 7
counterontransit = [0] * 7
piepackages = [0] * 3
transpergrade = [0] * 7

hashMap = {}

for k in range(0,N[n]):
    for v in range(0,H):
        hashMap["{}{}".format(k,v)] = [0] * K
       
#Garantiza que hay almenos un arribo al inicar la simulacion 
ta = -1
pg = 0
tsim = 0
final = 0
counter = 0

Pa = np.zeros((1,5))
contendientes = [0] * N[n] #nodos con el menor número de backoff
numPaquete = 0
x = 0
y = 0
z = 0

#Generacion de paquetes
for i in range (1,1330000 + 1):
    if ta < tsim:
        landa2 = landa[l]*N[n]*H
        U = (1e6*random())/1e6
        nuevot = -(1/landa2)*log10(1-U)
        nodo = randint(0,N[n]-1)
        grado = randint(0,H-1)

        if Nodos[nodo,grado] < K:
            Nodos[nodo,grado] = Nodos[nodo,grado] + 1
            llave = str(nodo) + str(grado)
            aux = hashMap[llave]
            index = [indice for indice, item1 in enumerate(aux) if item1 == 0]
            
            if index:
                pg = pg + 1
                aux[index[0]] = pg
                hashMap[llave] = aux
                aux = [0] * K           
    
        ta = tsim + nuevot

    if Decimal(str(i))%Decimal(str(Tcycle)) == 0:
        #Transmisión, recorremos desde nodo más alejado
        for grado in range(H-1,-1,-1):
            for nodo in range(0,N[n]):
                if(Nodos[nodo,grado] != 0):
                    contendientes[nodo] = randint(0,W[n]-1)
                else:
                    contendientes[nodo] = None
            #Colisiones
            #El contador más pequeño es el que transmite
            nodoGanador = min(filter(lambda x: x is not None, contendientes)) if any(contendientes) else None
            colisiones = [indice for indice, item in enumerate(contendientes) if item == nodoGanador]#busaca que contendientes tienen el mismo número de contador

            if len(colisiones) > 1:
                #Hay una colisión
                for index_colision in range(0,len(colisiones)):
                    #Eliminamos los paquetes que colisionaron
                    #Actualizar HASH
                    llaveHash1 = "{}{}".format(colisiones[index_colision],grado)
                    aux1 =  hashMap[llaveHash1]
                    #Pa[aux[0,0],4] = -1 #Actualizar Pa

                    #Pa = np.vstack([Pa,np.zeros((1,5))]) 
                    aux1.pop(0)
                    aux1.append(0)
                    hashMap[llaveHash1] = aux1

                    #Actualizar NODOS
                    Nodos[colisiones[index_colision], grado] = Nodos[colisiones[index_colision], grado] - 1
            else:
                #Revisar si hay algo que transmitir al menos un paquete en el grado.
                if nodoGanador:
                    #Restar al buffer del hashMap paquete del nodo (Grado I)
                    #print(nodoGanador)
                    #print(contendientes)
                    indexNodo = [indice for indice, item in enumerate(contendientes) if item == nodoGanador]
                    #print(indexNodo)
                    llaveHash2 = "{}{}".format(indexNodo[0],grado)
                    aux2 =  hashMap[llaveHash2]
                    numPaquete = aux2[0]
                    aux2.pop(0)
                    aux2.append(0)
                    hashMap[llaveHash2] = aux2
                    Nodos[indexNodo[0], grado] = Nodos[indexNodo[0], grado] - 1 #Actualizar matriz Nodos (grado I)

                    if grado - 1 != -1: #Sumar al buffer del hashMap paquete del nodo (Grado I -1)
                        llaveHash3 = "{}{}".format(indexNodo[0],grado - 1)
                        aux3 =  hashMap[llaveHash3]
                        a = [indice for indice, item1 in enumerate(aux3) if item1 == 0]
    
                        if a:
                            aux3[a[0]] = numPaquete
                            transpergrade[grado] = transpergrade[grado] + 1
                            hashMap[llaveHash3] =  aux3
                            Nodos[indexNodo, grado - 1] = Nodos[indexNodo, grado -1] + 1 #Actualizar matriz Nodos (grado I-1)
                        else:
                            x += 1
                            pass
                    
                    else:
                        transpergrade[grado] = transpergrade[grado] + 1
        
        counter = counter +1

        #Termina Transmitir cada ciclo de trabajo.
    tsim = tsim + Tcycle