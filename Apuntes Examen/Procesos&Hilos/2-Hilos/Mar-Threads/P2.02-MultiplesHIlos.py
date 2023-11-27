import threading

def actividad(i):
  print ("Escribo desde un hilo" + str(i))
  return

print ("INICIO")
hilos = list() #lista de hilos
for i in range(50):
  t = threading.Thread(target=actividad,args=(i,)) # creo el hilo y le asigno la función
  hilos.append(t) #añado el hilo a la lista
  t.start() #lanzo el hilo
print ("ESCRIBO EN PRINCIPAL")
