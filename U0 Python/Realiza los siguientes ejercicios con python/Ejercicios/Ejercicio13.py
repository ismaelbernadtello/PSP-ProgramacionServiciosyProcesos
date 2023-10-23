# Ejercicio 13: 
#     Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix, que contenga los siguientes métodos: 
#         - getNumberRows(): devuelve el número de filas de la matriz.
#         - getNumberColumns(): devuelve el número de columnas de la matriz.
#         - setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el valor de [element].
#         - addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los elementos de [matrix], 
#                                     y el resultado se almacena en la matriz inicial. 
#                                     Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial, la operación no se puede realizar (notificalo).
#         - multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual a los elementos de [matrix], 
#                                     y el resultado se almacena en la matriz inicial. 
#                                     Si [matrix] no tiene el mismo número de filas y columnas que la matriz inicial, la operación no se puede realizar (notificalo).

class Matriz:
    def __init__(self, filas, columnas): 
        self.filas = filas 
        self.columnas = columnas 
        self.matriz = [[0 for j in range(columnas)] for i in range(filas)] 
    
    def getNumeroFilas(self): 
        return self.filas 
    
    def getNumeroColumnas(self): 
        return self.columnas 
    
    def setElemento(self, x, j, elemento): 
        self.matriz[x][j] = elemento 
    
    def sumarMatriz(self, matriz): 
        if len(matriz) != self.filas or len(matriz[0]) != self.columnas: 
            print("Error: la matriz argumento no tiene el mismo tamaño que la matriz actual.") 
            return 
        for i in range(self.filas): 
            for j in range(self.columnas): 
                self.matriz[i][j] += matriz[i][j] 
    
    def multiplicarMatriz(self, matriz): 
        if len(matriz) != self.columnas: 
            print("Error: el número de filas de la matriz argumento no coincide con el número de columnas de la matriz actual.") 
            return 
        resultado = [[0 for j in range(len(matriz[0]))] for i in range(self.filas)] 
        for i in range(self.filas): 
            for j in range(len(matriz[0])): 
                for k in range(self.columnas): 
                    resultado[i][j] += self.matriz[i][k] * matriz[k][j] 
        self.matriz = resultado
        
        
# Pruebo Todas las funciones de la clase, Te quiero mucho copilot <3

# Crear una instancia de la clase Matriz
mi_matriz = Matriz(3, 3)

# Imprimir el número de filas y columnas de la matriz
print("Número de filas:", mi_matriz.getNumeroFilas())
print("Número de columnas:", mi_matriz.getNumeroColumnas())

# Establecer elementos en la matriz
mi_matriz.setElemento(0, 0, 1)
mi_matriz.setElemento(0, 1, 2)
mi_matriz.setElemento(0, 2, 3)
mi_matriz.setElemento(1, 0, 4)
mi_matriz.setElemento(1, 1, 5)
mi_matriz.setElemento(1, 2, 6)
mi_matriz.setElemento(2, 0, 7)
mi_matriz.setElemento(2, 1, 8)
mi_matriz.setElemento(2, 2, 9)

# Imprimir la matriz
print("Matriz original:")
for fila in mi_matriz.matriz:
    print(fila)

# Sumar otra matriz a la matriz actual
otra_matriz = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
mi_matriz.sumarMatriz(otra_matriz)

# Imprimir la matriz después de la suma
print("Matriz después de la suma:")
for fila in mi_matriz.matriz:
    print(fila)

# Multiplicar la matriz actual por otra matriz
otra_matriz = [[2, 2], [2, 2], [2, 2]]
mi_matriz.multiplicarMatriz(otra_matriz)

# Imprimir la matriz después de la multiplicación
print("Matriz después de la multiplicación:")
for fila in mi_matriz.matriz:
    print(fila)

