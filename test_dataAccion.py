import unittest
import random
import json
import numpy as np
from fileAction import *
'''self.assertEqual(c.calculate(valuesTest2[j-1],i), first_Number)'''


class Test_Create(unittest.TestCase):
    def testingCreate(self):
        name = surname ='Test'
        age = 90
        email = 'Test@'
        
        data = json.loads(open("data.json","r").read())
        a = FileAction.create(name,surname,age,email)
        keyValues = np.array(list(data.keys()))

        
        self.assertIn(name,keyValues)

if __name__ == "__main__":
    unittest.main()
