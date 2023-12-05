# Exercise 4: Cree un programa que ejecute 10 hilos, cada uno de los cuales sumará 100 números aleatorios entre el 1 y el 1000. 
# Muestre el resultado de cada hilo. Ganará el hilo que consiga el número mas alto

import threading
import random

def sumar_numeros_aleatorios(): #Funcion que suma 100 numeros aleatorios entre 1 y 1000
    numbers = [random.randint(1, 1000) for _ in range(100)]
    result = sum(numbers) #Suma de numeros aleatorios
    print(f"Thread {threading.current_thread().name}: {result}") #Mostrar resultado de la suma del hilo


#Lista de hilos
threads = []

for i in range(10): #Creacion de 10 hilos
    thread = threading.Thread(target=sumar_numeros_aleatorios) #Creacion de hilo y asignacion de funcion
    threads.append(thread) #Añadir hilo a la lista
    thread.start() #Inicio hilo

for thread in threads:
    thread.join() #Esperar a que todos los hilos terminen