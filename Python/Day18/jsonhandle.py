# Day 19 - JSON

import json

# Python dictionary
person = {
    "name": "Grace",
    "age": 21,
    "is_student": True
}

# Convert Python to JSON
json_data = json.dumps(person)

print(json_data)
print(type(json_data))

# Convert JSON to Python
python_data = json.loads(json_data)

print(python_data)
print(type(python_data))

# Pretty printing
formatted = json.dumps(person, indent=4)

print(formatted)

# Write JSON to file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Read JSON from file
with open("person.json", "r") as file:
    data = json.load(file)

print(data)

# JSON list
students = [
    {"name": "Grace", "marks": 95},
    {"name": "Emma", "marks": 88}
]

json_students = json.dumps(students, indent=4)

print(json_students)

# Access values
print(data["name"])
print(data["age"])

# Add new key
data["country"] = "India"

print(data)

# Remove key
del data["age"]

print(data)