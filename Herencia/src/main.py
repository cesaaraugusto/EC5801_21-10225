class punto():
    def __init__(self,x,y,z):
        self.__x:int=x
        self.__y:int=y
        self.__z:int=z

    def getCoordenadas(self): # Función getter
        coordenadas:int = [self.__x,self.__y,self.__z] 
        return coordenadas
    
    def __add__(self, other):
        if(isinstance(other, (int))): # Suma escalar
            return punto(self.getCoordenadas()[0] + other,self.getCoordenadas()[1] + other,self.getCoordenadas()[2] + other)
        else: # Suma puntos
            return punto(self.getCoordenadas()[0] + other.getCoordenadas()[0],self.getCoordenadas()[1] + other.getCoordenadas()[1],self.getCoordenadas()[2] + other.getCoordenadas()[2])

    def __sub__(self, other):
        if(isinstance(other, (int))): # Resta escalar
            return punto(self.getCoordenadas()[0] - other,self.getCoordenadas()[1] - other,self.getCoordenadas()[2] - other)
        else: # Resta puntos
            return punto(self.getCoordenadas()[0] - other.getCoordenadas()[0],self.getCoordenadas()[1] - other.getCoordenadas()[1],self.getCoordenadas()[2] - other.getCoordenadas()[2])

    def __mul__(self, other):
        if(isinstance(other, (int))): # Resta escalar
            return punto(self.getCoordenadas()[0] * other,self.getCoordenadas()[1] * other,self.getCoordenadas()[2] * other)
        else: # Resta puntos
            return punto(self.getCoordenadas()[0] * other.getCoordenadas()[0],self.getCoordenadas()[1] * other.getCoordenadas()[1],self.getCoordenadas()[2] * other.getCoordenadas()[2])
        
class vector(punto):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)

    def magnitud(self): # Calculo magnitud vector
        return (self.getCoordenadas()[0]**2 + self.getCoordenadas()[1]**2+self.getCoordenadas()[2]**2)**(1/2)

# Ejemplo suma por escalar y de puntos
puntoA = punto(0,0,0)
puntoB = punto(1,2,3)
puntoC = puntoA + puntoB
print(f"{puntoC.getCoordenadas()}")
puntoD = puntoA + 5
print(f"{puntoD.getCoordenadas()}")

# Ejemplo resta por escalar y de puntos
puntoE = punto(3,2,1)
puntoF = punto(1,2,3)
puntoG = puntoE - puntoF
print(f"{puntoG.getCoordenadas()}")
puntoH = puntoE - 5
print(f"{puntoH.getCoordenadas()}")

# Ejemplo producto escalar
puntoI = punto(5,4,3)
puntoJ = punto(1,2,3)
puntoK = puntoI * puntoJ
print(f"{puntoK.getCoordenadas()}")
puntoL = puntoI * 5
print(f"{puntoL.getCoordenadas()}")

#Ejemplo vector
vectorA = vector(1,2,2)
print(f"{vectorA.magnitud()}")