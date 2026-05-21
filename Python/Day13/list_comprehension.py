#What is List Comprehension? A shorter way to create lists.
numbers= [i for i in range(5)]#[new_value for item in iterable]
print(numbers)

# Day 13 - List Comprehension

# Basic list comprehension
numbers = [i for i in range(5)]
print(numbers)

# Multiply numbers
nums = [x * 2 for x in range(5)]
print(nums)

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Odd numbers
odds = [x for x in range(10) if x % 2 != 0]
print(odds)

# Square numbers
squares = [x * x for x in range(6)]
print(squares)

# String list
names = ["grace", "john", "emma"]

upper_names = [name.upper() for name in names]
print(upper_names)

# Length of words
lengths = [len(word) for word in names]
print(lengths)

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]

flat = [num for row in nested for num in row]
print(flat)#for each row, for each num

# Conditional expression
numbers = [x if x % 2 == 0 else "odd" for x in range(5)]
print(numbers)