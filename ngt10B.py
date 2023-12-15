#json parse
import json
#some json text:
employee ='{"name":"rahul","age":30,"city":"mumbai"}'
#convert it into python object:
data = json.loads(employee)
print(data["name"],data["age"])
#parsing json
