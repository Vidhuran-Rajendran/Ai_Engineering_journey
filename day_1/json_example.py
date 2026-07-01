import json

student = {
    "name": "jhon",
    "age": 34}
student["marks"] = 23847
with open("data.json","w") as file:
    json.dump(student,file)

with open("data.json", "r") as file:
    data = json.load(file)
print(data)


