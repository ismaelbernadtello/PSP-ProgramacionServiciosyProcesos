# Ejercicio 6:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) 
# y muestre por pantalla dicha cadena, pero con el primer y último carácter cambiados de posición.

cadena = input("Introduce una cadena de caracteres: ")
print("La cadena introducida es:", cadena)


""" Obtengo el primer carácter de la cadena con cadena[0] y el final con cadena[-1]
Y el resto de la cadena con cadena [1:-1] que es lo mismo que cadena[1:len(cadena)-1] """

print("La cadena con el primer y último carácter cambiados de posición es:", cadena[-1] + cadena[1:-1] + cadena[0])