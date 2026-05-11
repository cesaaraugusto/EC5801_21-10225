class matriz():
    def __init__(self,M,N): # Constructor de clase
        self.filas:int=M # Atributo filas
        self.columnas:int=N # Atributo columnas
        self.matriz:int= [[0 for i in range(N)] for j in range(M)] # Inicialización matriz vacía

    def imprimir(self):
        for j in range(self.filas): # Se recorre cada fila
            print("|",end="")
            for i in range(self.columnas): # Se recorre cada columna
                if (i == self.columnas-1):
                    print(f"{self.matriz[j][i]:>4}", end="|") # Se imprime el elemento final alineado dentro de una tabulación   
                else:
                    print(f"{self.matriz[j][i]:>4}", end="\t") # Se imprime el elemento alineado dentro de una tabulación
            print("") # Salto de línea
        print("")

    def __add__(self, other):
        if (self.filas != other.filas or self.columnas != other.columnas): # Verificación de mismo tamaño
            print("Las matrices son de distinto tamaño")
            return None
        else:
            matrizResultado:int = matriz(self.filas, self.columnas) # Inicialización matriz resultado
            for j in range(matrizResultado.filas): # Se recorre cada fila
                for i in range(matrizResultado.columnas): # Se recorre cada columna
                    matrizResultado.matriz[j][i]=self.matriz[j][i]+other.matriz[j][i] # Suma elemento con elemento
            return matrizResultado
        
    def __sub__(self, other):
        if (self.filas != other.filas or self.columnas != other.columnas): # Verificación de mismo tamaño
            print("Las matrices son de distinto tamaño")
            return None
        else:
            matrizResultado:int = matriz(self.filas, self.columnas) # Inicialización matriz resultado
            for j in range(matrizResultado.filas): # Se recorre cada fila
                for i in range(matrizResultado.columnas): # Se recorre cada columna
                    matrizResultado.matriz[j][i]=self.matriz[j][i]-other.matriz[j][i] # Suma elemento con elemento
            return matrizResultado
        
    def __mul__(self, other):
        if (self.columnas != other.filas): # Verificación
            print("Las matrices no se pueden multiplicar")
            return None
        else:
            matrizResultado:int = matriz(self.filas, other.columnas) # Inicialización matriz resultado
            for j in range(matrizResultado.filas): # Se recorre cada fila
                for i in range(matrizResultado.columnas): # Se recorre cada columna
                    for n in range(other.filas): # Formula para calcula elemento de la matriz resultado
                        matrizResultado.matriz[j][i] += self.matriz[j][n] * other.matriz[n][i]
            return matrizResultado
        
    def __truediv__(self, other):
        raise ValueError("Las matrices no se pueden dividir")

# Ejemplo Suma
matrizPrimerSumando = matriz(2,2)
matrizPrimerSumando.matriz[0][0] = 1
matrizPrimerSumando.matriz[1][1] = 1
matrizSegundoSumando = matriz(2,2)
matrizSegundoSumando.matriz[0][1] = 1
matrizSegundoSumando.matriz[1][0] = 1
matrizSuma = matrizPrimerSumando + matrizSegundoSumando
matrizSuma.imprimir()

# Ejemplo Resta
matrizPrimerRestando = matriz(2,2)
matrizPrimerRestando.matriz[0][0] = 1
matrizPrimerRestando.matriz[1][1] = 1
matrizSegundoRestando = matriz(2,2)
matrizSegundoRestando.matriz[0][1] = 1
matrizSegundoRestando.matriz[1][0] = 1
matrizResta = matrizPrimerRestando - matrizSegundoRestando
matrizResta.imprimir()

# Ejemplo Multiplicación
matrizPrimerMultiplicando = matriz(2,2)
matrizPrimerMultiplicando.matriz[0][0] = 1
matrizPrimerMultiplicando.matriz[1][1] = 1
matrizSegundoMultiplicando = matriz(2,2)
matrizSegundoMultiplicando.matriz[0][1] = 1
matrizSegundoMultiplicando.matriz[1][0] = 1
matrizMultiplicacion = matrizPrimerMultiplicando * matrizSegundoMultiplicando
matrizMultiplicacion.imprimir()

# Ejemplo División
matrizPrimerDividendo = matriz(2,2)
matrizPrimerDividendo.matriz[0][0] = 1
matrizPrimerDividendo.matriz[1][1] = 1
matrizSegundoDividendo = matriz(2,2)
matrizSegundoDividendo.matriz[0][1] = 1
matrizSegundoDividendo.matriz[1][0] = 1
matrizDivision = matrizPrimerDividendo / matrizSegundoDividendo
matrizDivision.imprimir()