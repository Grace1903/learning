# Day 1 - Python Basics

print("Hello Grace!")

# Basic maths
print(2 + 3)
print(10 - 5)
print(3 * 4)
print(10 / 2)

# Variables
name = "Grace"
age = 21
country = "India"

print(name)
print(age)
print(country)

# Data types
print(type(name))
print(type(age))
print(type(country))
city = "Kochi"
course= "CSE"

print(city)
print(course)


'''
# Day 1 Errors

## NameError

Wrong:
print(place)

Reason:
Variable not defined

Correct:
place = "Kerala"
print(place)
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(name)
print(age)
print(height)

print(type(name))
print(type(age))
print(type(height))
'''
Enter your name: Grace
Enter your age: 22
Enter your height: 160
Grace
22
160.0
<class 'str'>
<class 'int'>
<class 'float'>
'''


age = input("Enter age")#no int 
print(age + 1)#TypeError: can only concatenate str (not "int") to str