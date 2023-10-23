# Ejercicio 11: Tenemos la siguiente tabla multidimensional,
# la cual almacena por cada una de sus filas el salario trimestral de cada uno de los empleados de la empresa.

# int salarios[][] = { {700, 900, 1300} , {1000, 950, 1080}, {1300, 930, 1200} }
# A su vez, disponemos también de una tabla empleados, con los nombres de los trabajadores:
# String empleados[] = {Javier María, Antonio Muñoz, Isabel Allende}
# Implementa un programa Python que muestre por pantalla lo siguiente:
# Javier Marías -> 700 + 900 + 1300 = 2900€
# Antonio Muñoz -> 1000 + 950 + 1080 = 3030€
# Isabel Allende -> 1300 + 930 + 1200 = 3430€

# Declaro la lista de listas salarios
salarios = [[700, 900, 1300], [1000, 950, 1080], [1300, 930, 1200]]
empleados = ['Javier María', 'Antonio Muñoz', 'Isabel Allende']

# Recorro la lista de listas salarios y voy sumando los elementos de cada lista
for i in range(len(empleados)):
    salario_total = sum(salarios[i])
    # Imprimo el resultado
    print(f"{empleados[i]} -> {salarios[i][0]} + {salarios[i][1]} + {salarios[i][2]} = {salario_total}€")
    