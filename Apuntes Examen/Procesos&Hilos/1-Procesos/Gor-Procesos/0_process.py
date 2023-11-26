import multiprocessing
import random
import string

# Establece la semilla para que los resultados sean reproducibles, es decir siempre tocan los mismo números aleatorios
# Es como los mundos de Minecraft, si pones la misma semilla, siempre te saldrá el mismo mapa
random.seed(123)

def crea_frase(length, output):
    # Genera una frase aleatoria de longitud length, y la pone en la cola output
    # La frase se compone de letras mayúsculas, minúsculas y números del 0 al 9
    frase = ''.join(random.choice(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.digits)
                    for i in range(length))
    output.put(frase)


if __name__ == "__main__":
    
    output = multiprocessing.Queue()

    processes = [multiprocessing.Process(target=crea_frase, args=(10, output)) for x in range(4)]
                # Output que vamos a ver: ['nVphyT9FYe', '6H28x2JPZS', 'a4UO2A16Jt', 'YG8L0vAfoL']
                
    for p in processes:
        p.start()
    for p in processes:
        p.join()    #El programa principal espera a que todos los procesos hijos terminen antes de continuar

    results = [output.get() for p in processes] #La función get() se utiliza para extraer elementos de la cola.
    print(results)


"""
La cola se utiliza para recopilar resultados de los procesos hijos 
y permitir al proceso principal acceder a esos resultados una vez 
que los procesos hayan terminado.
"""