from abc import ABC, abstractmethod
import json

class DataAccion(ABC):
    
        
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
