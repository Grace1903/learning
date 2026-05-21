#A function is a reusable block of code.Instead of writing same code again and again:write once → use many times
#add(1, 2, 3)- Error only add(1,2) but use *
#*args means “take ANY number of arguments”

# Day 11 - Functions

# Simple function
def greet():
    print("Hello Grace")

greet()

# Function with parameter
def greet_user(name):
    print("Hello", name)

greet_user("Grace")

# Function with multiple parameters
def add(a, b):
    print(a + b)

add(5, 3)

# Function returning value
def square(num):
    return num * num

result = square(4)
print(result)

# Default parameter
def country(name="India"):
    print(name)

country()
country("Japan")

# Keyword arguments
def person(name, age):
    print(name, age)

person(age=21, name="Grace")

# Arbitrary arguments (*args)
def total_sum(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))

# Function with list
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

fruit_list = ["apple", "banana", "mango"]

print_fruits(fruit_list)

# Even or odd
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(4))
print(check_even(7))

# Lambda function
square = lambda x: x * x

print(square(5))