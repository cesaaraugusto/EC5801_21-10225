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
        if (self.path.exists() == False):
            return print("Ruta no valida")

        if (self.__is_binary(self.path) == True):
            with self.path.open('rb'):
                contenido = self.path.read_bytes()
            return contenido
        else:
            with self.path.open('r'):
                contenido = self.path.read_text('utf-8')
            return contenido
    
    def write_file(self, data: Union[str, bytes]):
        if (isinstance(data,bytes)):
            if(self.path.exists()==True):
                with self.path.open("ab"):
                    contenido = self.path.open("ab").write(data)
            else:
                contenido = self.path.write_bytes(data)
        else:
            if(self.path.exists()==True):
                with self.path.open("a"):
                    contenido = self.path.open("a",encoding="utf-8").write(data)
            else:
                contenido = self.path.write_text(data, encoding="utf-8")