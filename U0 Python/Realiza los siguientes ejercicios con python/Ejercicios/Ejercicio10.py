# Ejercicio 10:  Implementa un método Python llamado mayorYmenor, 
# el cual recibe como parámetro una tabla de Strings 
# y muestra por pantalla el String con mayor longitud y el String con menor longitud.

def mayorYmenor(tabla):
    mayor = ""
    menor = tabla[0]
    for string in tabla:
        if len(string) > len(mayor):
            mayor = string
        if len(string) < len(menor):
            menor = string
    print("El string con mayor longitud es:", mayor)
    print("El string con menor longitud es:", menor)
