# Exercise 2: Using the multithreading module, write a python program as follows:
# ● Create a pool of threads to run concurrent tasks.
# ● The pool size should be 3.
# ● Create and fill an array of 100 random integer numbers.
# ● Run all 3 threads to parse the vector data. One of them must show the mean, another
#   the maximum and minimum value, and the last one the standard deviation. Note that
#   although these processes share the vector, they only do so for reading. None of them
#   must modify any value of the vector.
import threading
import random
import statistics

# Crear y llenar un array de 100 números enteros aleatorios
vector = [random.randint(1, 100) for _ in range(100)]

# Función que muestra el promedio del vector
def calcular_promedio():
    promedio = statistics.mean(vector)
    print(f"El promedio del vector es: {promedio}")

# Función que muestra el máximo y mínimo valor del vector
def encontrar_maximo_y_minimo():
    maximo = max(vector)
    minimo = min(vector)
    print(f"El máximo valor del vector es: {maximo}")
    print(f"El mínimo valor del vector es: {minimo}")

# Función que muestra la desviación estándar del vector
def calcular_desviacion_estandar():
    desviacion_estandar = statistics.stdev(vector)
    print(f"La desviación estándar del vector es: {desviacion_estandar}")

if __name__ == "__main__":
    # Crear un conjunto de hilos
    hilos = [
        threading.Thread(target=calcular_promedio),
        threading.Thread(target=encontrar_maximo_y_minimo),
        threading.Thread(target=calcular_desviacion_estandar)
    ]

    # Iniciar todos los hilos
    for hilo in hilos:
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("Todos los hilos han terminado.")
