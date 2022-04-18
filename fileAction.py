from abc import ABC, abstractmethod
import json

from fileJson import FileJson
from save import Save


class FileAction(FileJson):
    def __init__(self):
        super().__init__(self.data)
    def create(self,name,surname,age,email):
        dataJson = NotImplemented
        
        self.data[name]= {
            'Name':name,
            'Surname': surname,
            'Age': age,
            'Email': email
        }

        Save().saving(self.data)


    def delete(self,name):
        del(self.data[name])
        Save().saving(self.data)

    def update(self,name,surname,age,email):
        self.data[name] = {
            'Name':name,
            'Surname': surname,
            'Age': age,
            'Email': email
        }
        Save().saving(self.data)

    def getInfo(self):
        return self.data
