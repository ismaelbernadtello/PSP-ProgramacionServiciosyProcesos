# Ejercicio 15: 
#     Crea un fichero de texto con el nombre y contenido que tú desees. Por ejemplo, Ejercicio15.txt. 

#     Realiza un programa en Python que lea el fichero <<Ejercicio15.txt>> y muestre su contenido por pantalla sin espacios.

#     Por ejemplo, si el fichero contiene el siguiente texto “Hola que haces”, deberá mostrar “Holaquehaces”.

# Creamos el archivo de texto con el contenido deseado
with open("Ejercicio15.txt", "w") as f:
    f.write("Hola que haces")

# Leemos el archivo y eliminamos los espacios en blanco del contenido con el método replace()
with open("Ejercicio15.txt", "r") as f:
    contenido = f.read().replace(" ", "")

# Mostramos el contenido sin espacios por pantalla
print(contenido)
