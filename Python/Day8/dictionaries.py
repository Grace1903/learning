# Day 8 - Dictionaries

# Creating dictionary
person = {
    "first_name": "Grace",
    "last_name": "Elizabeth",
    "country": "India",
    "age": 21,
    "is_student": True
}

print(person)

# Accessing values
print(person["first_name"])
print(person["age"])

# Using get()
print(person.get("country"))

# Adding new item
person["city"] = "Kochi"
print(person)

# Modifying value
person["age"] = 22
print(person)

# Length of dictionary
print(len(person))

# Check key exists
print("age" in person)

# Removing item
person.pop("is_student")
print(person)

# keys()
print(person.keys())

# values()
print(person.values())

# items()
print(person.items())

# Looping through dictionary
for key, value in person.items():#items necessary
    print(key, value)

'''
person = {
    "name": "Grace",
    "age": 21
}

for key, value in person():
    print(key, value)

Error:

TypeError: 'dict' object is not callable
'''
# Copy dictionary
new_person = person.copy()
print(new_person)

# Clear dictionary
temp = {
    "a": 1,
    "b": 2
}

temp.clear()
print(temp)

# Creating dictionary
person = {
    "first_name": "Grace",
    "last_name": "Elizabeth",
    "country": "India",
    "age": 21,
    "is_student": True
}

print(person)

# Accessing values
print(person["first_name"])
print(person["age"])

# Using get()
print(person.get("country"))

# Adding new item
person["city"] = "Kochi"
print(person)

# Modifying value
person["age"] = 22
print(person)

# update()
person.update({
    "college": "XYZ College"
})

print(person)

# Length of dictionary
print(len(person))

# Check key exists
print("age" in person)

# Removing item using pop()
person.pop("is_student")
print(person)

# Removing item using del
del person["city"]
print(person)

# keys()
print(person.keys())

# values()
print(person.values())

# items()
print(person.items())

# Loop through keys and values
for key, value in person.items():
    print(key, value)

# Loop through only keys
for key in person:
    print(key)

# Loop through only values
for value in person.values():
    print(value)

# Copy dictionary
new_person = person.copy()
print(new_person)

# Clear dictionary
temp = {
    "a": 1,
    "b": 2
}

temp.clear()
print(temp)

# Nested dictionary
student = {
    "name": "Grace",
    "marks": {
        "math": 95,
        "science": 90,
        "english": 88
    }
}

print(student)

# Access nested value
print(student["marks"]["math"])

# Print all subjects and marks
for subject, mark in student["marks"].items():
    print(subject, mark)

# Formatted printing
for subject, mark in student["marks"].items():
    print(f"{subject} : {mark}")

# Remove specific subject using del
del student["marks"]["math"]

print(student)

# Add it back
student["marks"]["math"] = 95

print(student)

# Remove using pop()
removed_mark = student["marks"].pop("science")

print(removed_mark)
print(student)

# Dictionary from input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

user = {
    "name": name,
    "age": age
}

print(user)