class matriz():
    def __init__(self,M,N): # Constructor de clase
        self.filas=M # Atributo filas
        self.columnas=N # Atributo columnas
        self.matriz:int= [[0 for i in range(N)] for j in range(M)] # Inicialización matriz vacía

    def imprimir(self):
        for j in range(self.filas): # Se recorre cada fila
            print("|",end="")
            for i in range(self.columnas): # Se recorre cada columna
                if (i == self.columnas-1):
                    print(f"{self.matriz[j][i]}", end="|") # Se imprime el elemento final    
                else:
                    print(f"{self.matriz[j][i]}", end="\t") # Se imprime el elemento
            print("") # Salto de línea

    def __add__(self, other):
        if (self.filas != other.filas or self.columnas != other.columnas): # Verificación de mismo tamaño
            print("Las matrices son de distinto tamaño")
            return None
        else:
            matrizResultado = matriz(self.filas, self.columnas) # Inicialización matriz resultado
            for j in range(matrizResultado.filas): # Se recorre cada fila
                for i in range(matrizResultado.columnas): # Se recorre cada columna
                    matrizResultado.matriz[j][i]=self.matriz[j][i]+other.matriz[j][i] # Suma elemento con elemento
            return matrizResultado
        
    def __sub__(self, other):
        if (self.filas != other.filas or self.columnas != other.columnas): # Verificación de mismo tamaño
            print("Las matrices son de distinto tamaño")
            return None
        else:
            matrizResultado = matriz(self.filas, self.columnas) # Inicialización matriz resultado
            for j in range(matrizResultado.filas): # Se recorre cada fila
                for i in range(matrizResultado.columnas): # Se recorre cada columna
                    matrizResultado.matriz[j][i]=self.matriz[j][i]-other.matriz[j][i] # Suma elemento con elemento
            return matrizResultado
        
    def __mul__(self, other):
        if (self.columnas != other.filas): # Verificación
            print("Las matrices no se pueden multiplicar")
            return None
        else:
            matrizResultado = matriz(self.filas, other.columnas) # Inicialización matriz resultado
            for j in range(matrizResultado.filas): # Se recorre cada fila
                for i in range(matrizResultado.columnas): # Se recorre cada columna
                    for n in range(other.filas): # Formula para calcula elemento de la matriz resultado
                        matrizResultado.matriz[j][i] += self.matriz[j][n] * other.matriz[n][i]
            return matrizResultado
        
    def __truediv__(self, other):
        raise ValueError("Las matrices no se pueden dividir")

matrizTest = matriz(2,3)
matrizTest.matriz[0][0]=1
matrizTest.matriz[1][0]=1
matrizSecundaria = matriz(3,1)
matrizSecundaria.matriz[0][0]=1
matrizResultado = matrizTest / matrizSecundaria
matrizResultado.imprimir()
