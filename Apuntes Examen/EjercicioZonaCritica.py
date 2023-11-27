import os, psutil, time, subprocess, multiprocessing, sys
import threading
import tempfile
# Crea un archivo temporal con un nombre aleatorio. El archivo se borrará automáticamente cuando se cierre.
file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

def mimetodo(nota,lock):
# Open the file for writing.
    time.sleep(1)
    
    #La ventaja de usar el bloque with lock: es que se encarga automáticamente de adquirir y liberar el bloqueo, 
    # incluso si ocurre una excepción dentro del bloque. 
    # Es más legible y reduce la posibilidad de errores al gestionar manualmente la adquisición y liberación del bloqueo.
    #Sería lo mismo que tener un lock.acquire() y un lock.release() en el código.
    with lock:
        subprocess.run(["ping", "-c", "4", "google.com"])   # Limit the number of pings to 4
        time.sleep(1)
        with open(file_name, 'w') as f:
            print("guardando en "+file_name)
            f.write("mi nota del examen es un "+str(nota))

# llama  a mi metodo usando hilos
lock = threading.Lock()
h = threading.Thread(target=mimetodo, args=(1,lock,))
h.start()

h1 = threading.Thread(target=mimetodo, args=(2,lock,))
h1.start()

h2 = threading.Thread(target=mimetodo, args=(3,lock,))
h2.start()

h3 = threading.Thread(target=mimetodo, args=(4,lock,))
h3.start()

h4 = threading.Thread(target=mimetodo, args=(10000,lock,))
h4.start()

h.join()
h1.join()
h2.join()
h3.join()
h4.join()

# dado ese código, acelera la ejecución mediante hilos(ya os lo he dado hecho. en el examen tendreis que añadirlo)
# consigue que la salida salga ordenada usando locks para cubrir aquella seccion crítica