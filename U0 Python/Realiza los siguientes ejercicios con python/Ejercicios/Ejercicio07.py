# Ejercicio 7:  Implementa un programa Python que solicite al usuario una cadena de caracteres 
# y devuelva dicha cadena, pero al revés.

cadena = input("Introduce una cadena de caracteres: ")
print("La cadena introducida es:", cadena)

# La función reversed() devuelve un iterador que recorre la secuencia en orden inverso.
# Uso la función join() para concatenar las letras de la cadena al revés.

print("La cadena al revés es:", ''.join(reversed(cadena)));