# Ejercicio 14: Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
#                 - 1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.
#                 - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
#                 - 3. Salir del Programa.

def write_numbers():
    with open("pares.txt", "w") as file:
        for i in range(0, 101, 2):
            file.write(str(i) + "\n")
    print("Archivo creado con éxito.")

def read_file():
    try:
        with open("pares.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("El archivo no existe.")

def main():
    while True:
        print("Menú:")
        print("1. Volcado (escritura) de una lista con todos los números pares comprendidos entre 0 y 100.")
        print("2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.")
        print("3. Salir del Programa.")
        option = input("Seleccione una opción: ")
        if option == "1":
            write_numbers()
        elif option == "2":
            read_file()
        elif option == "3":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
