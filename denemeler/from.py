import json
import types

indexjson = open("index.json")
data = json.load(indexjson)
keys = []
userMessages = []
unknownMessages = []
serverMessages = []
for i in data:
    keys.append(i)

for x in keys:
    if type(data[x]) == types.NoneType:
        unknownMessages.append("c"+x)
    elif "Direct Message" in data[x]:
        userMessages.append("c"+x)
    else:
        serverMessages.append("c"+x)