import threading
import queue
import time
import random

q = queue.Queue()

#Todas las clases tienen que extender de threading.Thread
class Productor(threading.Thread):
    #Es el método constructor
    #LLama al constructor de la clase padre y llamar a una cola 
    def __init__ (self, q, x): # 
        threading.Thread.__init__(self)
        self.q = q
        self.x = x
        
    def run(self):
        while True: # Va a poner un 1 en la cola
            #Si se piden generar números aleatorios es con el random.randint(1,100)
            #Si se piden generar varios productores cada vez se hace otro self.q.put() o se ponen dentro de un for
            self.q.put(1)       
            self.q.put(2)  
            self.q.put(random.randint(1,100)) # Genera un numero aleatorio entre 1 y 10    

            #Cada productor va a meter x elementos en la cola con un valor aleatorio entre 1 y 100
            for i in range(x):
                self.q.put(random.randint(1,100))

            # Espera 1 segundo antes de meter más elementos en la cola 
            time.sleep(1) #Producer Time 'PT'
            
            # Convierto los elementos de la lista en string para poder imprimirlos
            print("contenido de la cola:" + str(list(self.q.queue))) # Imprime los elementos de la cola


# Va a imprimir/sacar un numero de la cola
class Consumidor(threading.Thread):
    #Es el método constructor
    #LLama al constructor de la clase padre y llamar a una cola 
    def __init__ (self, q): # 
        threading.Thread.__init__(self)
        self.q = q
        
    def run(self):
        while True: # Va a sacar un numero de la cola
            a = self.q.get()
            b = self.q.get() #Si quiero sacar 2 elementos de la cola, tengo que llamar 2 veces a la funcion get
            print("contenido de la cola: " + str(a) + " y " +str(b)) # Imprime los elementos de la cola
            print("Imprime la suma de los 2 números que saca de la cola = " + str(a+b))
            time.sleep(2) # Espera 1 segundo antes de sacar otro elemento de la cola
            #Producer Time 'CT'


#Relacion 1:1 sería así:
#p = Productor(q)
#c = Consumidor(q)

#Relación 5:2 sería así:
#p = Productor(q, 5)
#p = Productor(q, 5)
#p = Productor(q, 5)
#p = Productor(q, 5)
#p = Productor(q, 5)
#c = Consumidor(q, 2)
#c = Consumidor(q, 2)


#Esto va a inicializar las clases
# p = Productor(q)
# c = Consumidor(q)
# Si quieres crear mas productores y consumidores, solo tienes que crear mas objetos
# c2 = Consumidor(q)

#Ejercicio1
CN = 2
PN = 3

#Si queremos usar un método para crear N productores y  N consumidores
def start(CN,PN):
    #CN = Consumer Number (Número de consumidores)
    for i in range(CN):
        c = Consumidor(q)
        c.start()
        c.join()

    #PN = Producer Number (Número de productores)
    for i in range(PN):
        p = Productor(q, 5)
        p.start()
        p.join()
# Llamamos al método
start(CN,PN)

#Esto va a ejecutar/arrancar las clases
# p.start()
# c.start()
# c2.start()

#Esto va a esperar a que las clases terminen
# p.join()
# c.join()
# c2.join()
