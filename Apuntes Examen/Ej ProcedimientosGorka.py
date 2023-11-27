"""
Crea dos procesos, y lístalos usando psutil
El primer proceso estará 10 segundos vivo y matará al otro proceso,
finalmente creará un fork de si mismo.
El segundo proceso a los 5 segundos cambiará la prioriodad del primer proceso.
y lanzará el comando ping a la web de google
"""
import subprocess
import psutil,time,os,multiprocessing

def proceso_1():
    #Creo el proceso
    print("Proceso 1 creado correctamente.")
    
    # Esperar 10 segundos
    for i in range(10):
        print("Esperando los 10 segundos, segundos actual: " + str(i+1))
        time.sleep(1)
    
    #Para evitar que se haga un bucle infinito de forks
    if os.fork() == 0:
        print("Fork creado correctamente.")
        os._exit(0)
    

def proceso_2():
    # Creo el proceso
    print("Proceso 2 creado correctamente.")
    
    # Esperar 5 segundos
    for i in range(5):
        print("Esperando los 5 segundos, segundo actual: " + str(i+1))
        time.sleep(1)
    
    # Cambiar la prioridad del primer proceso
    print("Prioridad del proceso 1: " + str(psutil.Process(proceso1.pid).nice()))
    psutil.Process(proceso1.pid).nice(10)
    print("Prioridad del proceso 1 cambiada correctamente, nueva prioridad: " + str(psutil.Process(proceso1.pid).nice()))
    
    # Lanzar el comando ping a la web de google
    try:
        resultado_ping = subprocess.run(["ping", "-c", "4", "google.com"], check=True, capture_output=True)
        print("Resultado del ping a google.com:")
        print(resultado_ping.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error al hacer ping a google.com: {e.stderr.decode()}")


if __name__ == "__main__":
    #Creo el primer proceso
    proceso1 = multiprocessing.Process(target=proceso_1,name="proceso1")
    proceso2 = multiprocessing.Process(target=proceso_2,name="proceso2")
    
    # Creo el segundo proceso
    
    proceso1.start()
    proceso2.start()
    
    proceso1.join()
    
    # Cuando termina el primer proceso se mata al otro proceso
    try:
        for proc in psutil.process_iter():
            if proc.pid == proceso2.pid:
                print("Proceso a matar: " + str(proc.pid))
                proc.kill()
                print("Proceso matado correctamente.")
                break
    except psutil.NoSuchProcess:
        print("No existe un proceso con el PID " + str(proceso2.pid))
        
    proceso2.join()
    
    print("Terminado")