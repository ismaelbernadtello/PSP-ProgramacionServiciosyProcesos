# Ejercicio 8:  Implementa un programa Python con un método llamado sum(int [] tabla) que muestre por pantalla 
# el resultado de sumar todos los elementos de la tabla pasada como parámetro.


# Declaro la función sum() que recibe como parámetro una lista de enteros
def sum(tabla):
    # Declaro la variable donde sumo todos los elementos de la lista
    suma = 0
    # Recorro la lista y voy sumando los elementos
    for i in tabla:
        suma += i
    # Devuelvo el resultado de la suma
    return suma

# Pruebo la función sum() con una lista de números
numeros = [1, 2, 3, 4, 5]
resultado = sum(numeros)
print(resultado)