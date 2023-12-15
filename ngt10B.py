import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

print( person_dict)


print(person_dict['languages'])
#parsing
print(person_dict["name"])
