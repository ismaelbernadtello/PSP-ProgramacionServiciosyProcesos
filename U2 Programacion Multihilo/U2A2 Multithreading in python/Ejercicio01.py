# Exercise 1: Using the multithreading module, write a simple python program as follows:
# ● Create a pool of threads to run concurrent tasks.
# ● The pool size should be 10.
# ● The thread should receive as input a number [id] (unique identifier for each of the
#   threads, starting from 1) and a number [number_of_writtings] (number of times the
#   thread will write the message).
# ● Each thread should sleep a random amount of time (between 100 and 300
#   milliseconds) and write the message ("I am 1", "I am 2", etc) a random number of times
#   between 5 and 15.
import threading
import random
import time

# Función que cada hilo ejecutará
def tarea_hilo(id_hilo, numero_escrituras):
    for _ in range(numero_escrituras):
        # Duerme durante un tiempo aleatorio entre 100 y 300 milisegundos
        time.sleep(random.uniform(0.1, 0.3))
        print(f"Soy el hilo {id_hilo}")

# Función para crear un conjunto de hilos
def crear_pool_de_hilos(tamano_pool):
    hilos = []
    for i in range(1, tamano_pool + 1):
        # Número aleatorio de veces que el hilo escribirá el mensaje
        numero_escrituras = random.randint(5, 15)
        hilo = threading.Thread(target=tarea_hilo, args=(i, numero_escrituras))
        hilos.append(hilo)
    return hilos

if __name__ == "__main__":
    tamano_pool = 10
    pool_de_hilos = crear_pool_de_hilos(tamano_pool)

    # Inicia todos los hilos
    for hilo in pool_de_hilos:
        hilo.start()

    # Espera a que todos los hilos terminen
    for hilo in pool_de_hilos:
        hilo.join()

    print("Todos los hilos han terminado.")
