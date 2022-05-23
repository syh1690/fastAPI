import json

with open ('sampledata.json') as json_file:
    data = json.load(json_file)

    print(data)