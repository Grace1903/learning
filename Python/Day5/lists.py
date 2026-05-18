#LIST
#ordered, changeable collection.
nums = [10, 20, 30, 40, 50]

nums.append(60)#end of list
nums.insert(2, 25)#ordered
nums.remove(40)

print(nums)
print(len(nums))#6

for n in nums:
    print(n)
    # Day 5 - Lists

# Creating lists
fruits = ["apple", "banana", "mango"]
print(fruits)

# Different data types in list
mixed = ["Grace", 21, 8.5, True]
print(mixed)

# Indexing
print(fruits[0])
print(fruits[-1])

# Modifying list
fruits[1] = "orange"
print(fruits)

# Adding items
fruits.append("grape")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

# Removing items
fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

# Length of list
print(len(fruits))

# Check item exists
print("banana" in fruits)

# Looping
for fruit in fruits:
    print(fruit)

# Slicing
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])

# Sort list
nums = [5, 2, 9, 1, 7]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# sorted() (does NOT change original)
nums2 = [3, 1, 4, 2]
print(sorted(nums2))#dont change nums2 values
print(nums2)

# Copy list
new_list = fruits.copy()
print(new_list)

# Join lists
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# Repeat list
print([1, 2, 3] * 2)

# index()
#print(fruits.index("banana"))#ValueError: 'banana' is not in list

# enumerate()
for i, fruit in enumerate(fruits):
    print(i, fruit)
    '''
    Important understanding
Expression	Meaning
a * 2	repeat list 2 times
a + a	join lists
2 * a	same as a * 2

a = [1, 2, 3]

result = [x * 2 for x in a]
print(result)....to multiply each element by 2

Python uses 0-based indexing
else u can use...
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
    '''