from pathlib import Path

from yaml import load, dump

from file_manager import file_manager

class file_manager_yaml(file_manager):
    
    def __init__(self, path: Path):
        super().__init__(path)