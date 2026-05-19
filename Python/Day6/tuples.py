# Day 6 - Tuples

# Creating tuples
empty_tuple = ()
print(empty_tuple)

fruits = ("apple", "banana", "mango")
print(fruits)

# Tuple with different data types
info = ("Grace", 21, 5.8, True)
print(info)

# Accessing elements
print(fruits[0])
print(fruits[-1])

# Slicing tuple
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])

# Length of tuple
print(len(fruits))

# Check item exists
print("banana" in fruits)

# Tuple is immutable (cannot change)
# fruits[0] = "grape"  # ❌ This will give error

# Convert tuple to list
fruits_list = list(fruits)
print(fruits_list)

# Modify list then convert back
fruits_list.append("grape")
fruits = tuple(fruits_list)
print(fruits)
'''
fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)
fruits_list[0] = "grape"

print(fruits_list)
'''

# Tuple unpacking
person = ("Grace", 21, "India")

name, age, country = person

print(name)
print(age)
print(country)

# Count and index
nums = (1, 2, 2, 3, 4, 2)

print(nums.count(2))
print(nums.index(3))