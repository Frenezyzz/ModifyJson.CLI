from abc import ABC, abstractmethod
import json


from save import Save


class FileAction(DataAccion):
    def __init__(self):
        self.data = json.loads(open("data.json","r").read())
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
