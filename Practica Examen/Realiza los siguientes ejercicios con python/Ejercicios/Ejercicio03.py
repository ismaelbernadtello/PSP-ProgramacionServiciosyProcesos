# Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número. 
# El programa generará un número aleatorio entre 0 y 20 
# y luego irá pidiendo números al usuario indicando “mayor” o “menor” según sea mayor o menor con respecto al número generado aleatoriamente. 
# El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones junto al número de intentos que ha necesitado el usuario.

"""Creo un número aleatorio entre 0 y 20"""
from random import randint
aleatorio = randint(0,20)

acierto = False
num_intentos = 0

while not acierto:
    respuesta = int(input("¿Dime un número del 1 al 20, si lo aciertas has ganado?"))
    num_intentos += 1
    
    if int(respuesta) == aleatorio: # Si el usuario acierta, se muestra un mensaje de felicitaciones junto al número de intentos que ha necesitado el usuario.
        print("Enhorabuena, has adivinado el número en", num_intentos, "intentos, el número aleatorio era:", aleatorio)
        acierto = True
        
    else: # Si el usuario no acierta, se muestra un mensaje de si el número es mayor o menor que el aleatorio.
        if respuesta < aleatorio:
            print(respuesta, "es menor al número aleatorio, llevas",num_intentos,"intento(s)")
        else:
            print(respuesta, "es mayor al número aleatorio, llevas",num_intentos,"intento(s)")
        
