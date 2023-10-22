# Ejercicio 1: Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y) 
# y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos, con el siguiente formato:
#     x + y = …
#     x – y = …
#     x * y = …
#     x / y = …
#     x % y = …

""" Pido los números al usuario """
print("Introduce el primer número: ");
x = int(input());
print("Introduce el segundo número: ");
y = int(input());

""" Muestro los resultados de las operaciones"""
print(x, "+", y, "=", x+y); """ Suma """
print(x, "-", y, "=", x-y); """ Resta """
print(x, "*", y, "=", x*y); """ Multiplicación """
print(x, "/", y, "=", x/y); """ División """
print(x, "%", y, "=", x%y); """ Resto """