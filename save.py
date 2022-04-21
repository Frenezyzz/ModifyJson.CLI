
import json

class Save():
    def saving(self,data):
        dataJson = json.dumps(data, indent=4)

        fileJson = open("data.json","w")
        fileJson.write(dataJson)
        fileJson.close()
