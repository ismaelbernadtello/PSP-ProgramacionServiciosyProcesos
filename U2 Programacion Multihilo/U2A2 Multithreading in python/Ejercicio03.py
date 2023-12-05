# Exercise 3: Cree un hilo que genere números aleatorios entre 1 y 100 y los vaya insertando en una lista, 
# y otro que recorra circularmente esa lista y sustituya los números terminados en cero por el valor -1. 
# Un tercer hilo abortará los otros dos en el momento en el que la suma de los elementos de la lista supere el valor de 20000

import random
import threading

# Lista compartida entre los hilos
numbers_list = []

#Sirve para sumar los numeros aleatorios
sum_value = 0

# Semáforo para sincronizar el acceso a la lista
lock = threading.Lock()

# Función para generar números aleatorios y añadirlos a la lista
def generate_numbers():
    global sum_value
    while sum_value <= 20000:
        number = random.randint(1, 100)
        with lock:
            numbers_list.append(number) #Añado un número a la lista
            sum_value += number # Sumo el número al total

# Función para recorrer la lista y sustituir los números terminados en cero por -1
def replace_numbers():
    global sum_value
    while sum_value <= 20000:
        with lock:
            for i in range(len(numbers_list)):
                if numbers_list[i] % 10 == 0: #Si el resto del número entre 10 es 0 quiere decir que termina en 0
                    numbers_list[i] = -1

# Función para abortar los otros dos hilos cuando la suma supere 20000
def abort_threads():
    global sum_value
    while sum_value <= 20000:
        pass
    print("Suma de elementos superó 20000. Abortando hilos...")
    thread1.join()
    thread2.join()

# Creación de los hilos
thread1 = threading.Thread(target=generate_numbers)
thread2 = threading.Thread(target=replace_numbers)
thread3 = threading.Thread(target=abort_threads)

# Inicio de los hilos
thread1.start()
thread2.start()
thread3.start()

# Espera a que los hilos terminen
thread1.join()
thread2.join()
thread3.join()

# Imprimir la lista resultante
print("Lista resultante:", numbers_list)