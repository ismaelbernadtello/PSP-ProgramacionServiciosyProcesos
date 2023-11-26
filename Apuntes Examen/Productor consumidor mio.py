# Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:  
# -El productor produce números enteros mayor que 10 y menor que 1000, 
# el productor produce 10 números cada vez que los almacena en la cola 
# y el tiempo de espera entre la generación de un número y otro es de PT segundos (1 punto)  
# -El consumidor lee X números de la cola de golpe, calcula el MCD de esos X números .(1,5 punto)  

# el tiempo de espera entre la lectura de X elementos cola 
# y la siguiente lectura de los siguientes X elementos es de  CT segundos (1 punto)  
# Prueba el algoritmo con los distintos casos 
# usando una relación de productor:consumidor de:     

# - 1:1   con PT=1  CT=4 y X=3 (0,5 puntos)
# - 4:2 con PT=2  CT=4 y X=2 (0,5 puntos)
# - 2:10 con PT=1  CT=10 y X=4 (0,5 puntos)

# NOTA DAR UN PEQUEÑO TIEMPO ENTRE EL START DE CADA CONSUMIDOR Y/O PRODUCTOR Y EL SIGUIENTE PARA PODER VER BIEN LOS MENSAJES DEL PRINT

import math
import threading
import queue
import time
import random

#Esto es la cola de procesos para el consumidor y el productor
q = queue.Queue()

#Clase del productor
class Productor(threading.Thread):
    #Es el método constructor
    #LLama al constructor de la clase padre y llamar a una cola 
    def __init__ (self, q, PT): # 
        threading.Thread.__init__(self)
        self.q = q
        self.pt = PT
        
    def run(self):
        while True: 
            #Cada productor va a meter 10 elementos en la cola con un valor aleatorio entre 1 y 100
            for i in range(10):
                self.q.put(random.randint(11,999))
                print("Creando num aleatorio en el productor, num: " + str(i))

            # Imprime los elementos de la cola
            # Convierto los elementos de la lista en string para poder imprimirlos
            print("contenido de la cola:" + str(list(self.q.queue))) 
            
            #Producer Time 'PT'
            time.sleep(self.pt) 
            

#Clase del consumidor
class Consumidor(threading.Thread):
    #Es el método constructor
    #LLama al constructor de la clase padre y llamar a una cola 
    def __init__ (self, q,CT, X): # 
        threading.Thread.__init__(self)
        self.q = q
        self.ct = CT
        self.x = X
        
    def calcularMCD(self,listaMCD):
        # Calcula el Maximo comun divisor de los numeros de la lista
        mcd = listaMCD[0]
        for i in range(1,len(listaMCD)):
            mcd = math.gcd(mcd, listaMCD[i])
        print("El MCD de los numeros de la lista es: " + str(mcd))
        
    def run(self):
        while True: 
            # Sacar X elementos de la cola
            listaMCD = []
            for i in range(self.x):
                listaMCD.append(self.q.get())
                print("Imprimiendo numero de la cola con el consumidor" + str(listaMCD[i]))
            
            self.calcularMCD(listaMCD)
                
            #Producer Time 'CT'
            time.sleep(self.ct)





def start(numProductores, numConsumidores, PT, CT, X):
    productores = []
    consumidores = []
    
    for i in range(numProductores):
        p = Productor(q,PT)
        print("Creando productor")
        p.start()
        productores.append(p)
        
    for i in range(numConsumidores):
        c = Consumidor(q,CT,X)
        print("Creando consumidor")
        c.start()
        consumidores.append(c)
        
    for p in productores:
        p.join()
        
    for c in consumidores:
        c.join()



# - 1:1   con PT=1  CT=4 y X=3 (0,5 puntos)
numProductores = 1
numConsumidores = 1
PT = 1
CT = 4
X = 3
start(numProductores, numConsumidores, PT, CT, X)


# - 4:2 con PT=2  CT=4 y X=2 (0,5 puntos)
numProductores = 4
numConsumidores = 2
PT = 2
CT = 4
X = 2
#start(numProductores, numConsumidores, PT, CT, X)

# - 2:10 con PT=1  CT=10 y X=4 (0,5 puntos)
numProductores = 2
numConsumidores = 10
PT = 1
CT = 10
X = 4
#start(numProductores, numConsumidores, PT, CT, X)






