# Ejercicio 2:  Escribe un programa Python que pregunte al usuario por 10 números enteros 
# y muestre por pantalla el número total de veces que el usuario ha introducido el 0, 
# el número total de enteros mayores que 0 introducidos
# y el número total de enteros menores que 0 introducidos.

"""Creo las listas para guardar los números"""""
numeros = []
numeros_menores_0 = []
numeros_mayores_0 = []

"""Pido los números y los guardo en la lista"""""
for i in range(10):
    numeros.append(int(input("Escribe un número entero...")))
print(numeros)

"""Voy contando los números y los guardo en la lista correspondiente para luego contarlos"""
for num in numeros:
    if num < 0:
        numeros_menores_0.append(num)
        
for num in numeros:
    if num > 0:
        numeros_mayores_0.append(num)
        


print('La cantidad de veces que has introducido el número 0 son: ', numeros.count(0))
print('La cantidad de veces que has introducido un número menor a 0 son: ', len(numeros_menores_0))
print('La cantidad de veces que has introducido un número mayor a 0 son: ', len(numeros_mayores_0))
