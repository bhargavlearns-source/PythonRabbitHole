'''
Python datatypes are types of objects.
'''

#variables
'''
The varibales in python are easy to understand!
variables are the names which are reffering to the memory location where the object is stored!
when we do a = 10, here a is the name which is reffering to the int object 10.
if we do a = 12 later on in our python program, a will be the name which will be reffering to the int object 12.

In short, variables are the names which are bound to an object, it doesnt contains the objects itself.
'''
#Numbers
a = 10 #int 
print(type(a)) #type() is a build in function in python which takes the variable name and return its type.
b = 9.9 #float
print(type(b))

#Strings
a = "Hello world" #This is a string object (btw for curiosity now a is reffering to a string object)
print(a[3]) #print the element at index 3, remember the counting starts from left to right and starts from 0!
print(a[1:3]) #this will print the elements from index 1 to 2 (it does not include 3)
print(a[1:4:2]) #this will start from 1 and goes to 3 and it will print every second element starts from 1
print(a.capitalize()) #This capitalize the first letter of the string object.
print(a.split(" ")) #This splits a string into list object, it takes the letter where you want to split.
print(a.count("l")) #This counts the number of time l appears in the string object a.

#list 
a = [1,2,3,4, "hello world", 3.3] #A list is a data type which can contain any data type object.
print(a[3]) #print the element at index 3, remember the counting starts from left to right and starts from 0!
print(a[1:3]) #this will print the elements from index 1 to 2 (it does not include 3)
print(a[1:4:2]) #this will start from 1 and goes to 3 and it will print every second element starts from 1
a.append(20)
print(a)
print(a.count(1))
b = [10,20,30,40]
a.extend(b)
print(a)
#When you print this section in your code editor, you will realise that 
#Many of the list methods literally change the actual list object which is reffered by variable a.
#This is the concept of mutability and immutability which we will encounter later on!


#Tuple
a = (1,2,3,4)
print(a[1]) #This is basic indexing
print(a.count(1)) #This will return the count of 1
print(a.index(2)) #This will return the index of int object 2


#dictionary
dic = {
    "name": "Bhargav",
    "Age": 19
}
#Another way of writing dictionary in your modules!
dic = {"name": "Bhargav","Age": 19}

#Dictionary is a data type which contains a key-value pair!
#Key must be immutable, which means string, tuple and numbers are the most commonly used keys in the dictionary!
#A key always reffer to a value in the dictionary which can be any object, every a dictionary it self.
#Here are few more examples of dictionaries, try to observe them:
dictionary_1 = {
    1: "bhargav",
    2: "Anurag",
    3: "Parthak"
}
print(dictionary_1[1]) #This will return the value which is there at that particular key
#Note: You should not make two or more keys with the same object
#example:
dictionary_2 ={
    1: "bhargav", 
    1: "anurag",
    1: "paru"
}
print(dictionary_2[1]) #this will return the value which is associated with the last key object matching the arugment key
# print(dictionary_2[2]) #this will return an error, because 2 is not a key in our dictionary yet!
print(dictionary_2.get(2)) #this will return None if the key doesnt exist, instead of raising an error
print(dictionary_2.items()) #this will return a tuple of (key,value) pair, however it will be dict item object.
#The results of dictionary_2.items() will shock you, it will return dict_items([(1, 'paru')])
#This means that 1:"bhargav", 1:"anurag", were never part of this dictionary, and only the 1 which was assigned in the last is part of the dict!
dictionary_2.pop(1) #This will pop the only remaining element in the dictionary 1:"paru"
print(dictionary_2.items()) #this will be empty
print(dictionary_2.keys()) #this will return keys
print(dictionary_2.values()) #this will return values

dictionary_3 = {
    "name": "bhargav",
    "age": 19
}
print(dictionary_3)
dictionary_3.clear() #this will clear the dictionary
print(dictionary_3) # this will return an empty dictionary


#sets
s = {1,2,33,44,44} # a set is a well-defined collection of different objects, considered as an object in its own right.
#set is mutable and it similar with the sets with we studied in our high school!
s.add(4)
print(s) #Notice 44 got printed once because set remove the dublicates that the main reason it is used.
emptyset = set() #This is the way to create empty set because {} will be empty dictionary
#It also have union and intersection.


# ============================================================
# PART II PRACTICE QUESTIONS — PYTHON DATA TYPES
# ============================================================


# ============================================================
# 1. NUMBERS
# ============================================================

# Q1. Digit Manipulation
# Given an integer:
# n = 583927
#
# Without converting it to a string:
# - Find the largest digit
# - Find the smallest digit
# - Find the sum of all digits
# - Reverse the number


# Q2. Armstrong Number
# Write a program to check whether a number is an Armstrong number.
#
# Example:
# 153 → True
# Because:
# 1³ + 5³ + 3³ = 153
#
# Make your solution work for numbers with ANY number of digits.


# Q3. Perfect Number
# Check whether a number is a perfect number.
#
# Example:
# 28 → True
# Because:
# 1 + 2 + 4 + 7 + 14 = 28
#
# Try to avoid checking unnecessary numbers.


# Q4. Number Classification
# Given a number, determine whether it is:
# - Prime
# - Composite
# - Perfect square
# - Palindrome
#
# Return all applicable properties.


# ============================================================
# 2. STRINGS
# ============================================================

# Q1. Character Frequency
# Given:
# s = "programming"
#
# Create a dictionary showing the frequency of every character.
#
# Do not use count().


# Q2. First Non-Repeating Character
# Given:
# s = "aabbcddeff"
#
# Find the first character that occurs only once.
#
# Expected:
# c


# Q3. Longest Word
# Given:
# sentence = "Python makes programming surprisingly enjoyable"
#
# Find the longest word.
#
# Bonus:
# What happens if multiple words have the same maximum length?


# Q4. String Compression
# Convert:
# "aaabbccccdaa"
#
# Into:
# "a3b2c4d1a2"
#
# Do not use external libraries.


# Q5. Palindrome Ignoring Formatting
# Check whether:
# "A man, a plan, a canal: Panama"
#
# Is a palindrome.
#
# Ignore:
# - Spaces
# - Punctuation
# - Uppercase/lowercase differences


# Q6. Longest Substring Without Repeating Characters
# Given:
# s = "abcabcbb"
#
# Find the length of the longest substring
# containing no repeated characters.
#
# Expected:
# 3


# ============================================================
# 3. LISTS
# ============================================================

# Q1. Remove Duplicates While Preserving Order
# Given:
# L = [1, 2, 2, 3, 1, 4, 3, 5]
#
# Expected:
# [1, 2, 3, 4, 5]


# Q2. Second Largest Unique Value
# Given:
# L = [10, 45, 20, 45, 30]
#
# Find the second largest UNIQUE value.
#
# Do not use:
# - sort()
# - sorted()

# Q3. Rotate a List
# Given:
# L = [1, 2, 3, 4, 5]
# k = 2
#
# Rotate the list right by k positions.
#
# Expected:
# [4, 5, 1, 2, 3]
#
# Make it work even when:
# k > len(L)


# Q4. Move Zeros
# Given:
# L = [0, 1, 0, 3, 12]
#
# Move all zeros to the end while maintaining
# the relative order of non-zero elements.
#
# Expected:
# [1, 3, 12, 0, 0]


# Q5. Find Duplicates
# Given:
# L = [4, 3, 2, 7, 8, 2, 3, 1]
#
# Find all elements that occur more than once.
#
# Expected:
# [2, 3]
#
# Bonus:
# Preserve the order in which duplicates first appear.


# ============================================================
# DICTIONARIES — PRACTICE
# ============================================================

# Q1. Character / Word Frequency
# Given:
# text = "python is easy and python is powerful"
#
# Create a dictionary showing how many times
# each word appears.
#
# Expected idea:
# {
#     "python": 2,
#     "is": 2,
#     ...
# }


# Q2. Invert a Dictionary With Duplicate Values
# Given:
# d = {
#     "a": 1,
#     "b": 2,
#     "c": 1,
#     "d": 2
# }
#
# Convert it to:
# {
#     1: ["a", "c"],
#     2: ["b", "d"]
# }


# Q3. Merge Dictionaries
# Given:
# d1 = {
#     "a": 10,
#     "b": 20
# }
#
# d2 = {
#     "b": 5,
#     "c": 30
# }
#
# Merge them so that values with the same key
# are added together.
#
# Expected:
# {
#     "a": 10,
#     "b": 25,
#     "c": 30
# }


# Q4. Nested Dictionary Lookup
# Given:
# data = {
#     "user": {
#         "profile": {
#             "name": "Bhargav",
#             "age": 19
#         }
#     }
# }
#
# Retrieve:
# - The name
# - The age
#
# Then try accessing the data safely using .get()
# so missing keys do not crash the program.


# ============================================================
# TUPLES — PRACTICE
# ============================================================

# Q1. Swap Variables
# Given:
# a = 10
# b = 20
#
# Swap them using tuple unpacking.
#
# Then explain conceptually what happens.


# Q2. Tuple Unpacking
# Given:
# data = ("Bhargav", 19, "India", "Python")
#
# Use tuple unpacking to store:
# - name
# - age
# - country
# - skill
#
# Then use extended unpacking to capture
# the middle values.


# Q3. Coordinate Calculations
# Given:
# p1 = (2, 3)
# p2 = (7, 11)
#
# Calculate:
# - Distance between the points
# - Midpoint



# ============================================================
# SETS — PRACTICE
# ============================================================

# Q1. Set Operations
# Given:
# A = [1, 2, 3, 4, 5]
# B = [4, 5, 6, 7, 8]
#
# Find:
# - Common elements
# - Elements only in A
# - Elements only in B
# - All unique elements


# Q2. Unique Words
# Given:
# text = "python is easy and python is powerful"
#
# Find:
# - Total number of words
# - Unique words
# - Number of repeated words


# Q3. Missing Numbers
# You have numbers from 1 to 20,
# but some numbers are missing from a list.
#
# Find all missing numbers efficiently using sets.


# ============================================================
# MIXED DATA TYPES — PRACTICE
# ============================================================

# Q1. Student Data Analysis
# Given:
#
# students = {
#     "Bhargav": {
#         "marks": [90, 85, 95],
#         "skills": {"Python", "Git", "NumPy"}
#     },
#
#     "Rahul": {
#         "marks": [70, 80, 75],
#         "skills": {"Python", "C"}
#     }
# }
#
# Find:
# 1. Each student's average marks
# 2. The highest-performing student
# 3. Students who know Python
# 4. Common skills between students


# Q2. Inventory Data Analysis
# Given:
#
# inventory = {
#     "Laptop": {
#         "price": 50000,
#         "quantity": 5
#     },
#
#     "Mouse": {
#         "price": 500,
#         "quantity": 20
#     }
# }
#
# Find:
# - Total value of the inventory
# - Most expensive product
# - Products with quantity below a chosen threshold


# Q3. Simple Data Cleaning
# Given:
#
# data = ["Python", "", "python", "AI", "Python", "", "ML", "ai"]
#
# Clean the data by:
# - Removing empty strings
# - Converting everything to lowercase
# - Removing duplicates
#
# Try to preserve the original order.


# ============================================================
# END OF PRACTICE
# ============================================================