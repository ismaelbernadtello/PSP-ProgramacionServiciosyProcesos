# Exercise 1: Using the multithreading module, write a simple python program as follows:
# ● Create a pool of process to run concurrent tasks.
# ● The pool size should be 10.
# ● The thread should receive as input a number [id] (unique identifier for each of the
#   threads, starting from 1) and a number [number_of_writtings] (number of times the
#   thread will write the message).
# ● Each thread should sleep a random amount of time (between 100 and 300
#   milliseconds) and write the message ("I am 1", "I am 2", etc) a random number of times
#   between 5 and 15.
import time, multiprocessing, random


def tarea_proceso(id_proceso,numero_escrituras):
    #Duerme durante un tiempo aleatorio entre 100 y 300 milisegundos
    time.sleep(random.uniform(0.1, 0.3))
    
    #Escribe el mensaje un número de veces aleatorio entre 5 y 15
    for i in range(numero_escrituras):
        #Imprime el mensaje
        print(f"Soy el proceso {id_proceso}")
        

def crearPoolDeProcesos():
    pool = multiprocessing.Pool(10)
    for i in range (10):
        print("creando el proceso", i)
        pool.apply_async(tarea_proceso, args=(i, random.randint(5, 15)))
    pool.close()
    pool.join()
    print("Todos los procesos han terminado.")

if __name__ == '__main__':
    crearPoolDeProcesos()