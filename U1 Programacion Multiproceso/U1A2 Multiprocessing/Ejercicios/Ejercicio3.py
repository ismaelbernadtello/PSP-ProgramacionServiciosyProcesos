# Exercise 3: List all process in operative system with PID, and allow termination of one by PID

import os
import signal

# Obtener la lista de todos los procesos en el sistema operativo
def listar_procesos():
    procesos = []
    for pid in os.listdir('/proc'):
        if pid.isdigit():
            try:
                with open(f'/proc/{pid}/comm') as f:
                    nombre = f.read().strip()
                procesos.append((pid, nombre))
            except FileNotFoundError:
                continue
    return procesos

# Mostrar la lista de procesos con su PID
def mostrar_procesos():
    procesos = listar_procesos()
    for pid, nombre in procesos:
        print(f'PID: {pid}, Nombre: {nombre}')

# Terminar un proceso dado su PID
def terminar_proceso(pid):
    try:
        os.kill(int(pid), signal.SIGTERM)
        print(f'Proceso con PID {pid} terminado exitosamente.')
    except OSError:
        print(f'No se pudo terminar el proceso con PID {pid}.')

# Ejecutar las funciones
mostrar_procesos()
pid_a_terminar = input('Ingrese el PID del proceso que desea terminar: ')
terminar_proceso(pid_a_terminar)
