import time

class __memory(): #clase padre de las memorias
    def __init__(self,N):
        self.storage:int = [0 for _ in range(N)] # Creación arreglo memoria
        self.offset:int = 0 # Posición de memoria
        self.delay:int = 0 # Tiempo de acceso

    def read(self, address):
        time.sleep(self.delay)
        return self.storage[address]

    def write(self, data, *address):
        time.sleep(self.delay)
        if(address != self.offset and address != ()):
            self.storage[int(address[0])] = data
        else:
            self.storage[self.offset] = data        
            self.offset += 1
        print(f"{data} guardado")

class sram(__memory):

    def __init__(self,N):
        super().__init__(N)
        self.delay = 0.2

class ram(__memory):
    
    def __init__(self,N):
        super().__init__(N)
        self.delay = 3

class hdd(__memory):
    def __init__(self,N):
        super().__init__(N)
        self.delay = 10

# Ejemplo uso

cache = sram(10)
memoria_ram = ram(20)
disco_duro = hdd(50)

cache.write(1)
cache.write(2)
cache.write(3)
cache.write(4,1)
print(f"{cache.read(1)}")

memoria_ram.write(1)
memoria_ram.write(2)
memoria_ram.write(3)
memoria_ram.write(4,1)
print(f"{memoria_ram.read(1)}")

disco_duro.write(1)
disco_duro.write(2)
disco_duro.write(3)
disco_duro.write(4,1)
print(f"{disco_duro.read(1)}")