# Ejercicio 9:  Implementa un programa Python con un método llamado indexContains(String[] tabla, String cadena) 
# que devuelva el índice de la tabla cuyo valor es igual al valor de “cadena”. 
# En caso de no haber ningún valor igual, devuelve -1

def indexContains(tabla, cadena):
    for i in range(len(tabla)):
        if tabla[i] == cadena:
            return i
    return -1
