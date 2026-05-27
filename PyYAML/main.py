from pathlib import Path

from yaml import load, dump



from file_manager import file_manager

from typing import TypeVar, Generic

#tipo generico
generic_t = TypeVar("generic_t")

class file_manager_yaml(file_manager, Generic[generic_t]):
    
    def __init__(self, path: Path):
        super().__init__(path)  # herencia constructor

    __diccionario:generic_t # declaracion diccionario privado

    def read_file_yaml(self) -> dict | None: 
        if (self.path.exists() == False or self.path.is_file() == False): # comprobación existencia archivo
            return print("Ruta no valida")
        
        with self.path.open('r', encoding="utf-8") as stream_datos:
            deserializacion = yaml.load(stream_datos, Loader= loader)
    