
# - Completa el código Python para la implementación del Productor-Consumidor.
# - Asegúrate de incluir mensajes de impresión (print) para mostrar claramente las acciones de producción y consumo.
# - Ejecuta el algoritmo con cada conjunto de parámetros proporcionado en las pruebas.
# - Da un pequeño tiempo entre el inicio de cada consumidor y/o productor para facilitar la visualización de los mensajes de impresión.
# Implementa en Python un código de Productor-Consumidor mediante una cola sincronizada que cumpla con las siguientes especificaciones:  
# Productor  

# - Genera números enteros aleatorios, siendo cada número mayor que 50 y menor que 2000.
# - Produce 15 números en cada iteración, almacenándolos en la cola.
# - El tiempo de espera entre la generación de un número y otro es de PT segundos.

# Consumidor

# - Lee X números de la cola de golpe.
# - Calcula la suma de los cuadrados de esos X números.
# - El tiempo de espera entre la lectura de X elementos de la cola y la siguiente lectura de los siguientes X elementos es de CT segundos.

# Parametros

# - Relación Productor:Consumidor para cada caso.
# - PT (tiempo de espera del productor entre generaciones de números).
# - CT (tiempo de espera del consumidor entre lecturas de elementos).
# - X (cantidad de elementos leídos por el consumidor en cada iteración).


# a. Relación 1:1 con PT=2, CT=6 y X=4.  
# b. Relación 5:2 con PT=1, CT=3 y X=5.  
# c. Relación 3:10 con PT=3, CT=8 y X=2.


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
            #Cada productor va a meter 15 elementos en la cola con un valor aleatorio entre 50 y 2000
            for i in range(15):
                self.q.put(random.randint(51,1999))
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
        
    def calculaCuadrados(self,listaCuadrados):
        # Calcula la suma de los cuadrados de los numeros de la lista
        suma = 0
        for i in range(len(listaCuadrados)):
            suma += listaCuadrados[i]**2
        print("La suma de los cuadrados de los numeros de la lista es: " + str(suma))
        
    def run(self):
        while True: 
            # Sacar X elementos de la cola
            listaCuadrados = []
            for i in range(self.x):
                listaCuadrados.append(self.q.get())
                print("Imprimiendo numero de la cola con el consumidor" + str(listaCuadrados[i]))
            
            #Calcula la suma de los cuadrados de los numeros que consume el consumidor
            self.calculaCuadrados(listaCuadrados)
                
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


# a. Relación 1:1 con PT=2, CT=6 y X=4.  
numProductores = 1
numConsumidores = 1
PT = 2
CT = 6
X = 4
start(numProductores, numConsumidores, PT, CT, X)

# b. Relación 5:2 con PT=1, CT=3 y X=5.  
numProductores = 5
numConsumidores = 2
PT = 1
CT = 3
X = 5
#start(numProductores, numConsumidores, PT, CT, X)

# c. Relación 3:10 con PT=3, CT=8 y X=2.
numProductores = 3
numConsumidores = 10
PT = 3
CT = 8
X = 2
#start(numProductores, numConsumidores, PT, CT, X)



