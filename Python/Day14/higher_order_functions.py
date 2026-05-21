"""What are Higher Order Functions?

Functions that:

take another function as input
OR return a function

Main functions:

map()
filter()
reduce()

Function	Purpose
map()	transform
filter()	select
reduce()	combine
map(int, input().split())	convert to integers
map(str.strip, words)	remove spaces
map(str.upper, names)	uppercase all
"""# Day 14 - Higher Order Functions

from functools import reduce

# map()
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)

# map with uppercase
names = ["grace", "emma", "john"]

upper_names = list(map(str.upper, names))

print(upper_names)

# map with normal function
def double(num):
    return num * 2

doubled = list(map(double, numbers))

print(doubled)

# filter()
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)

# filter positive numbers
numbers2 = [-2, -1, 0, 1, 2, 3]

positive = list(filter(lambda x: x > 0, numbers2))

print(positive)

# filter names with length > 4
names2 = ["Grace", "John", "Emma", "Alexander"]

long_names = list(filter(lambda x: len(x) > 4, names2))

print(long_names)

# reduce()
numbers3 = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, numbers3)

print(total)

# reduce multiplication
product = reduce(lambda x, y: x * y, numbers3)

print(product)

# all()
nums3 = [True, True, True]

print(all(nums3))

# any()
nums4 = [False, False, True]

print(any(nums4))

# sorted()
numbers4 = [5, 2, 8, 1]

print(sorted(numbers4))

# sorted descending
print(sorted(numbers4, reverse=True))

# sorted by length
words = ["apple", "kiwi", "banana", "grape"]

print(sorted(words, key=len))

# List comprehension vs map
squares2 = [x * x for x in range(5)]

print(squares2)


"""
Simple visualization of reduce funct
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
Important

x is usually:

previous result

y is:

next list item"""
