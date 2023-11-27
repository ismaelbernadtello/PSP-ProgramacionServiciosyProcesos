import logging
import threading
import time

def thread_Apellido(name):
  print (name + " Rodríguez")
  #print (name + " Rodríguez\n")
    
nombres = ["Julio", "Javier", "Eladio", "Jose", "Manuel"]
hilos = list()
for n in nombres:
  #args=(n,) es una tupla y la coma es necesaria para que sea tupla. Sirve para pasar argumentos a la funcion
  t = threading.Thread(target=thread_Apellido, args=(n,)) 
  hilos.append(t)
  t.start()