from pathlib import Path
from typing import TypeVar, Generic

class file_manager():

    def __init__(self, path: Path) -> None:
        self.path = path

    def __is_binary(self, file: Path) -> bool: # detección archivo binario
            try:
                with self.path.open('rb') as file_test: # apertura en modo binario
                    muestra_archivo = file_test.read(1024) # tomamos una muestra para analizarla

                    if not muestra_archivo: # comprobación de archivo vacío
                        return False
                    
                    if b'\x00' in muestra_archivo: # comprobación de existencia byte nulo
                        return True
                    
                    muestra_archivo.decode('utf-8') # comprobación de error UnicodeDecode Error propio de intentar decodificar un archivo binario
                    return False
            except UnicodeDecodeError:
                return True # Fallo al decodificar
            except Exception:
                return False # Fallo externo
    
    def read_file(self) -> None|bytes|str:    
        if (self.path.exists() == False): # comprobación existencia archivo
            return print("Ruta no valida")

        if (self.__is_binary(self.path) == True): # comprobación archivo binario
            with self.path.open('rb'):
                contenido = self.path.read_bytes() # lectura archivo binario
            return contenido
        else:
            with self.path.open('r'):
                contenido = self.path.read_text('utf-8') # lectura archivo texto
            return contenido
    
    def write_file(self, data: Union[str, bytes]):
        if (isinstance(data,bytes)):    # comprobación archivo binario
            if(self.path.exists()==True):   # comprobación para no sobreescribir
                with self.path.open("ab"):
                    contenido = self.path.open("ab").write(data) # bytes añadidos
            else:
                contenido = self.path.write_bytes(data) # texto añadido
        else:
            if(self.path.exists()==True):
                with self.path.open("a"):
                    contenido = self.path.open("a",encoding="utf-8").write(data)    # bytes añadidos
            else:
                contenido = self.path.write_text(data, encoding="utf-8")    # texto añadido

# prueba lectura
directorio_binario = Path("archivo_binario_prueba.bin")
directorio_texto = Path("archivo_texto_prueba.txt")
manejador_archivos_binarios = file_manager(directorio_binario)
print(manejador_archivos_binarios.read_file())
manejador_archivos_texto = file_manager(directorio_texto)
print(manejador_archivos_texto.read_file())

# prueba escritura
manejador_archivos_binarios.write_file(b'\x06')
print(manejador_archivos_binarios.read_file())
manejador_archivos_texto.write_file("\ny este es un archivo modificado por César García")
print(manejador_archivos_texto.read_file())