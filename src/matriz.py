import numpy

class matriz():
    def __init__(self,M,N): # Constructor de clase
        self.Matriz:int=numpy.zeros((M,N))

    def imprimir(self):
        for j in range(self.Filas):
            for i in range(self.Columnas):
                print(f"{self.Matriz[i][j]}", end="\t")
            print("\n")

matrizTest = matriz(2,3)
matriz.imprimir(matrizTest)
