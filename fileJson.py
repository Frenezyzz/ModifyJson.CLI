from abc import ABC, abstractmethod
import json
class FileJson(ABC):

    @abstractmethod
    def __init__(self):       
        self.data = json.loads(open("data.json","r").read())