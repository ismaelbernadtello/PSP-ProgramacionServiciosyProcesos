import threading
import queue

q = queue.Queue()

#Todas las clases tienen que extender de threading.Thread
class Productor(threading.Thread):
    #Es el método constructor
    #LLama al constructor de la clase padre y llamar a una cola 
    def __init__ (self, q): # 
        threading.Thread.__init__(self)
        self.q = q
        
    def run(self):
        pass
    
class Consumidor(threading.Thread):
    #Es el método constructor
    #LLama al constructor de la clase padre y llamar a una cola 
    def __init__ (self, q): # 
        threading.Thread.__init__(self)
        self.q = q
        
    def run(self):
        pass
    
#Esto va a inicializar las clases
p = Productor(q)
c = Consumidor(q)

#Esto va a ejecutar/arrancar las clases
p.start()
c.start()

#Esto va a esperar a que las clases terminen
p.join()
c.join()