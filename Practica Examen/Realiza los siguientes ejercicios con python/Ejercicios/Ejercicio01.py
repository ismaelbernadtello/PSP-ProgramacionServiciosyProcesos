# Ejercicio 1: Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y) 
# y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos, con el siguiente formato:
#     x + y = …
#     x – y = …
#     x * y = …
#     x / y = …
#     x % y = …

print("Dime 2 números enteros")
x = int(input("x: "))
y = int(input("y: "))

print("Esta es la suma de los 2 números :" + str(x + y))
print("Esta es la resta de los 2 números :" + str(x-y))
print("Esta es la multiplicación de los 2 números :" + str(x*y))
print(x/y)
print(x%y)
