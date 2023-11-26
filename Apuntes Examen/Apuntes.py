# Tipos de ejercicio para el examen:

# 1-Productor Consumidor
# 2-Locks


# MULTIPROCESSING   esto es lo que pido del TEMA 1
# 0_process.py  
# 1_syncProcesses.py  
# 2_pool.py  


import multiprocessing, os, psutil, threading

#Sirve para recorrer todos los procesos del sistema y poder acceder a sus atributos y métodos
psutil.process_iter() 

multiprocessing.Process.nice()  #Te dice la prioridad del proceso. Siendo el máximo -20 y el mínimo +19
multiprocessing.Process.kill()  #Se carga el proceso que le indicamos ejemplo: 

#Libreria que nos permite acceder a información del sistema y de los procesos para poder manipularlos, etc
#psuitl  

#crea un nuevo proceso duplicando el proceso actual. Crea un 'hijo del proceso'
os.fork()  

# Crea un proceso 
multiprocessing.Process.start() 

#Hace que el proceso espere a que termine el proceso anterior
multiprocessing.Process.join() 
    


"""Un bloqueo es un mecanismo de sincronización que se utiliza en programas multiproceso para evitar la ejecución simultánea de un fragmento de código por más de un hilo. 
Esto es particularmente útil cuando el código modifica algún dato o recurso compartido. 
El objeto  threading.Lock()  tiene dos métodos:  acquire()  y  release() . 
En resumen, estos métodos se utilizan para garantizar que solo un hilo ejecute cierto código a la vez, evitando posibles problemas en un contexto multiproceso."""

threading.lock.acquire()  #Se utiliza para adquirir un bloqueo. Cuando un hilo llama a este método, se bloqueará hasta que el bloqueo esté desbloqueado.

threading.lock.release()  #Se utiliza para liberar un bloqueo. Si hay otros hilos bloqueados esperando a que el bloqueo se desbloquee, se permite que uno de ellos continúe. 
#Si el bloqueo ya está desbloqueado, se genera una  RuntimeError . 
