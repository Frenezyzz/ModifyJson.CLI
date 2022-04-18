import json
import numpy as np
asd={
    'nomber':'juan'
}

asdd = asd

print(asdd)
data = json.loads(open("data.json","r").read())
asdd['quehacejuan'] = 'tont'
print(asdd)
print(np.array(list(data.keys())))
