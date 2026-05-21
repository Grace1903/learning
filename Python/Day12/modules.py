# Day 12 - Modules.....A module is simply:a Python file containing code

import mymodule

print(mymodule.greet("Grace"))
print(mymodule.add(5, 3))

from mymodule import greet

print(greet("Grace"))

from mymodule import greet, add

print(greet("Grace"))
print(add(2, 3))

import mymodule as mm

print(mm.add(10, 20))

import math

print(math.sqrt(25))
print(math.pi)
print(math.floor(4.9))
print(math.ceil(4.1))

import random

print(random.randint(1, 10))

fruits = ["apple", "banana", "mango"]

print(random.choice(fruits))

import statistics

nums = [1, 2, 3, 4, 5]

print(statistics.mean(nums))

import math

print(dir(math))#operations