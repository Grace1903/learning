"""
Exceptions are errors that happen while program runs.

Example:

dividing by zero
invalid input
file not found

Without handling:

program crashes
"""
# Day 15 - Exceptions

# SyntaxError example
# print("Hello"

# NameError
try:
    print(name)
except NameError:
    print("Variable not defined")

# TypeError
try:
    print(5 + "5")
except TypeError:
    print("Cannot add int and string")

# ValueError
try:
    num = int("abc")
except ValueError:
    print("Invalid integer")

# IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Index out of range")

# KeyError
try:
    person = {"name": "Grace"}
    print(person["age"])
except KeyError:
    print("Key not found")

# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Generic exception
try:
    number = int(input("Enter a number: "))
    print(number)
except Exception as e:
    print("Error:", e)

# else block
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid number")

# finally block
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
finally:
    print("This always runs")

# Multiple exceptions
try:
    num = int(input("Enter number: "))
    print(10 / num)

except ValueError:
    print("Please enter integer")

except ZeroDivisionError:
    print("Cannot divide by zero")