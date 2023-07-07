
import json

with open('dwsample1-json.json') as file:
    data = json.load(file) # convert json to python object


print(data)
print(type(data))

# Convert this data into json file

with open('convert.json', 'w') as file2:
    json.dump(data, file2)

