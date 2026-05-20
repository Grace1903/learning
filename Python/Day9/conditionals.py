# Day 9 - Conditionals

# Simple if
age = 21

if age >= 18:
    print("You are an adult")

# if else
num = 5

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if elif else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Nested if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

# Comparison operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators
x = 5

if x > 0 and x < 10:
    print("Single digit positive number")

if x > 0 or x == 0:
    print("Non negative")

if not False:
    print("This is True")

# User input condition
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Ternary operator
age = 17

message = "Adult" if age >= 18 else "Minor"
print(message)