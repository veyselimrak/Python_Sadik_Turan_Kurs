import json

person_string = '{"name" : "Ali" , "languages" : ["Python","C#"]}'

# #JSON String to Dict

print(type(person_string))
person_dict = json.loads(person_string)

print(person_dict)
print(type(person_dict))
print(person_dict["name"])
print(person_dict["languages"])

# #Dict to JSON String

person_string = json.dumps(person_dict)
result = json.dumps(person_dict, indent=4, sort_keys=True)
print(result)
print(person_string)
print(type(person_string))

#Dosya Okuma

with open("person.json") as file:
    data = json.load(file)
    print(data)

#Dosyaya Yazma

person_dict = { 
    "name ":"Ali",
    "languages": ["Python","C#"] 
    }

with open("person.json","w") as file:
    json.dump(person_dict,file)
