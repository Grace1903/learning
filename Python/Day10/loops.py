# Day 10 - Loops

# for loop with list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# for loop with string
word = "Python"

for letter in word:
    print(letter)

# range()
for i in range(5):
    print(i)

# range(start, stop)
for i in range(1, 6):
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)

# Sum of numbers
total = 0

for i in range(1, 6):
    total = total + i

print(total)

# while loop
count = 1

while count <= 5:
    print(count)
    count += 1

# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(6):
    if i == 3:
        continue
    print(i)

# Nested loops
for i in range(3):
    for j in range(2):
        print(i, j)

# Loop with else
for i in range(3):
    print(i)
else:
    print("Loop completed")

# Pass statement
for i in range(3):
    pass

# User input loop
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
    
    #count += 1,inside while is VERY important.Otherwise:infinite loop