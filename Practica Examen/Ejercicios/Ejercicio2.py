# Ejercicio 2: Utilizando el módulo multiprocessing, escribe un programa simple en Python de la siguiente manera:

# Crea un grupo de trabajadores para ejecutar tareas en paralelo.
# El tamaño del grupo debe ser 2.
# Escribe una función para ejecutar en paralelo, llámala print_cube.
# La función debe recibir como entrada un número [num]. Cuando se llame,
# la función imprimirá en la pantalla un mensaje en el siguiente formato:
#     "El cubo del número [num] es [cube]". Donde [cube] debe ser reemplazado por el cubo del número recibido como entrada.

# Escribe una función para ejecutar en paralelo, llámala print_square.
# La función debe recibir como entrada un número [num]. Cuando se llame,
# la función imprimirá en la pantalla un mensaje en el siguiente formato:
#     "El cuadrado del número [num] es [square]". Donde [square] debe ser reemplazado por el cuadrado del número recibido como entrada.

import multiprocessing

def print_cube(num):
    cube = num ** 3 # Saco el cubo del número
    print(f"El cubo del número {num} es {cube}")

def print_square(num):
    square = num ** 2 # Saco el cuadrado del número
    print(f"El cuadrado del número {num} es {square}")

if __name__ == "__main__":
    # Numero a calcular
    num = 5  
    
    # Crear un grupo de trabajadores para ejecutar tareas en paralelo.
    pool = multiprocessing.Pool(processes=2)
    
    # Ejecutar las funciones en paralelo usando la función apply_async
    pool.apply_async(print_cube, (num,))
    pool.apply_async(print_square, (num,))
    
    # Cerrar el grupo de trabajadores
    pool.close()
    pool.join()
