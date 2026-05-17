language = "python"

print(language.upper())
print(language.capitalize())

sentence = "i love python"

print(sentence.title())

text = "   Hello   "

print(text.strip())

msg = "I love Java"

print(msg.replace("Java", "Python"))

fruits = "apple banana mango"

print(fruits.strip())#beginning end spaces only 
print(fruits.split())#string to list
new_fruits = fruits.split()

print(type(new_fruits))#list

print(language.find("t"))#start from 0

# String indexing
language = "Python"

print(language[0])   # P
print(language[1])   # y
print(language[2])   # t
print(language[-1])  # n

# String slicing
print(language[0:3])  # Pyt
print(language[3:6])  # hon or 3::


# split()
fruits = "apple banana mango"
print(fruits.split())

# split with comma
data = "apple,banana,mango"
print(data.split(","))

# startswith()
print(language.startswith("Py"))

# endswith()
print(language.endswith("on"))

# count()
text3 = "python python python"
print(text3.count("python"))

# isalpha()
word2 = "Python"
print(word2.isalpha())

word3 = "Python123"
print(word3.isalpha())

# isdigit()
num = "12345"
print(num.isdigit())

num2 = "123a"
print(num2.isdigit())

# join()
fruit_list = ['apple', 'banana', 'mango']

print(" ".join(fruit_list))
print(", ".join(fruit_list))
#convert array to string
text = "Python"

print(text[-1::-1])#nohtyP
word = "programming"

# last character
print(word[-1])

# reverse word
print(word[::-1])

# middle part
print(word[3:7])

# check find
print(word.find("g"))

# split + join combo
sentence = "I love Python"
words = sentence.split()
print(words)
print("-".join(words))