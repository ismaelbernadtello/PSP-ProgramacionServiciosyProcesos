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
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for j in range(columns)] for i in range(rows)]

    def getNumberRows(self):
        return self.rows

    def getNumberColumns(self):
        return self.columns

    def setElement(self, x, j, element):
        self.matrix[x][j] = element

    def addMatrix(self, matrix):
        if len(matrix) != self.rows or len(matrix[0]) != self.columns:
            print("Error: la matriz argumento no tiene el mismo tamaño que la matriz actual.")
            return
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] += matrix[i][j]

    def multMatrix(self, matrix):
        if len(matrix) != self.columns:
            print("Error: el número de filas de la matriz argumento no coincide con el número de columnas de la matriz actual.")
            return
        result = [[0 for j in range(len(matrix[0]))] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(len(matrix[0])):
                for k in range(self.columns):
                    result[i][j] += self.matrix[i][k] * matrix[k][j]
        self.matrix = result