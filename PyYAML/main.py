from pathlib import Path

from yaml import load, dump

from file_manager import file_manager

from typing import TypeVar, Generic

#tipo generico
generic_t = TypeVar("generic_t")

class file_manager_yaml(file_manager, Generic[generic_t]):
    
    def __init__(self, path: Path):
        super().__init__(path)

    __diccionario:generic_t

    def read_file_yaml(self):
        