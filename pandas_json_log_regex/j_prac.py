
import json

file= '{"fruit": "Apple","size": "Large","color": "Red", "health" : "True"}'

data = json.loads(file) #convert string(which looks like json) into python dict

print(data)
print(type(data))

data2 = json.dumps(data) # convert python dict to json string

print(data2)
print(type(data2))

