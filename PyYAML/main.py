from pathlib import Path

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except:
    from yaml import Loader, Dumper

from file_manager import file_manager

from typing import Any

class file_manager_yaml(file_manager):
    
    def __init__(self, path: Path):
        super().__init__(path)  # herencia constructor
        self.__diccionario:dict[str, dict] = {} # declaracion diccionario privado

    def read_file_yaml(self, path_file:str) -> None: 
        if ((self.path / path_file).exists() == False or (self.path / path_file).is_file() == False): # comprobación existencia archivo
            return print("Ruta no valida")
        
        self.__diccionario[(self.path / path_file).name] = {"path":(self.path / path_file).name,"data":load((self.path / path_file).open('r', encoding="utf-8"), Loader= Loader)}# guardar yaml en diccionario privado

    def write_file_yaml(self,path_file:str, value:str, data: Any):
        if ((self.path / path_file).exists() == False or (self.path / path_file).is_file() == False): # comprobación existencia archivo
            return print("Ruta no valida")
        
        self.__diccionario[(self.path / path_file).name]["data"][value] = data # añade o sobreescribe valores de parámetros
        
    def getter_atribute_yaml(self, path_file:str, value:str):# obtener un valor de un parametro de un archivo yaml
        if ((self.path / path_file).exists() == False or (self.path / path_file).is_file() == False): # comprobación existencia archivo
            return print("Ruta no valida")
        
        if(value == (self.path / path_file).name): # obtener diccionario completo del archivo yaml
            print(self.__diccionario.get(value))
        elif (value == "path"):# obtener path
            print(self.__diccionario[(self.path / path_file).name].get(value))
        else: # obtener valor de parametro especifico
            print(self.__diccionario[(self.path / path_file).name]["data"].get(value))

    def save_file_yaml(self, path_file:str):
        dump(self.__diccionario[(self.path / path_file).name]["data"], (self.path / path_file).open('w', encoding="utf-8"),Dumper=Dumper,sort_keys=False)
            
# Ejemplo Uso    
manejador_yaml = file_manager_yaml(Path.cwd())
manejador_yaml.read_file_yaml("config.yaml")
manejador_yaml.getter_atribute_yaml("config.yaml", 'version')
manejador_yaml.write_file_yaml("config.yaml","instalador_paquetes","pip")
manejador_yaml.getter_atribute_yaml("config.yaml", 'instalador_paquetes')
manejador_yaml.save_file_yaml("config.yaml")
