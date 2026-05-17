# Day 2 - Variables and Built-in Functions
'''
first_name = "Grace"
last_name = "Elizabeth"
country = "India"
city = "Kochi"
age = 21
is_student = True

print(first_name)
print(last_name)
print(country)
print(city)
print(age)
print(is_student)
print(len("Grace"))#5
age = int(input("Enter your age: "))

print(age)
print(type(age))

Enter your age: 22.5
asked for int gave float input
    age = int(input("Enter your age: "))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: '22.5'

first_name, last_name, country = "Grace", "Elizabeth", "India"

print(first_name)
print(last_name)
print(country)
age = 21

print(str(age))
print(type(str(age)))
'''
num = int(5.76575849494040)

print(num)
num = float(5)
print(num)

first_name = "Grace"
last_name = "Elizabeth"

full_name = first_name + " " + last_name#string concat
print(full_name)

name = "Grace"
age = 21
#string formatting,f-string
print(f"My name is {name} and I am {age} years old")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
print(Name)#NameError ...u should hv typed name not Name