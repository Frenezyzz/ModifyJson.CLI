from abc import ABC, abstractmethod
import json
import fileJson
class DataAccion(fileJson.FileJson):
    
        
    @abstractmethod
    def create(self): 
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def getInfo(self):
        pass