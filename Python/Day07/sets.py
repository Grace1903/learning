# Day 7 - Sets (STRICT)

fruits = {"apple", "banana", "mango"}
print(fruits)

# Add item
fruits.add("orange")#set so no duplicate but append is a list so yes dupli

# Remove item
fruits.remove("banana")

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # union
print(A & B)  # intersection
print(A - B)  # difference