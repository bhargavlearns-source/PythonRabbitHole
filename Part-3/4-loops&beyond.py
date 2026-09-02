# Loops are of mainly 2 types in python
# While loops and For loops
# loops follows iteration protocol which we will discuss in depth in this file!

## While loop

x = 1

while x <= 5:
    print(x)
    x += 1

# While loops says that until x is less than equal to 5 executed my body and then break.
# while makes more sense to use when you have much information about where you want to stop.

# lets create a game using while loop! (You will love this!)

import random #DONT BE SCARED, I WILL EXPLAIN YOU THIS IN THE UPCOMING CHAPTERS. (I PROMISE)

random_number = random.randint(0, 100) #remember this will return a number from 0 to 100

guesscount = 0
while True:
    guess = int(input("Enter your guess:"))
    guesscount += 1 #We studied this just know it is guesscount = guesscount + 1

    if guess == random_number:
        print(f"You guess the number in {guesscount} tries!!!")
        break #Break statement helps to break the loop and come out of it

    elif guess > random_number:
        print("Try a lower number!")

    else:
        print("Try a higher number!")
    
# Try to observe the code ahead!
# we basically generated a random number and assigned it to a variable
# we are running an endless while loop because we dont know when to stop
# we are asking the user to enter an input and guess the number
# if the number we guess is higher we ask user to input a lower number
# if the number is lower we ask user to enter a higher number
# if the value of the number we enter is equals to the random number we win and break the loop

##For loop
for x in [1, 2, 3]:
    print(x)

#we use for loop when we need to iterate over an iterable object
#normal you will see range in the for loop, lets understand range in depth!
# range("start", "stop", "step size") 

x = range(5) #this simply means start from 0, goes till 4 and take the default step size which is 1
print("Type:", type(x)) #this will return <class 'range'> because range itself is a built in data type in python
#it doesnot store a list and keep the number as it is!
for i in range(5):
    print(i) # 0 1 2 3 4 

# now time to go into the rabbit hole!!!
# How for loops internally works in python?

# For this python uses an iteration protocol

#When we pass on range in for loop, python roughly do something like:

"""
range object
     ↓
iter(range)
     ↓
range iterator
     ↓
next()
     ↓
0
     ↓
next()
     ↓
1
     ↓
next()
     ↓
2
...
"""

# take this code exmaple
for i in range(5):
    print(i)

iterator = iter(range(3))
print("=" * 50)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) #this will raise a stop iteration error which for loops handles internally
'''
# We have not covered exceptions but try to observe this code:

it = iter([1, 2, 3])

while True:
    try:
        x = next(it)
        print(x)

    except StopIteration:
        break
'''
#You can use a for loop on any iterable object!
lista = [2,3,4,5,"Hallo", True]
for i in lista:
    print(i)

# Zip (we can literally combine two list!!!)
list1 = [2,3,4,4]
list2 = [3,4,5,6]
for i,j in zip(list1,list2):
    print(f"i:{i} & j: {j}")
    print(i+j) 

#enumerate (we can attach index)

for i,j in enumerate(list1):
    print(f"i:{i} & j: {j}") #here i represents the index and #j represents the element



## list comprehension (BEST THING YOU WILL LEARN IN THIS REPO AFTER OOPS)

lista = [x for x in range(4)] #just observe we are basically doing [element_you_want_in_your_list for element in whatever thing]
print(lista)
lista = [x**2 for x in range(4)] #square the numbers
print(lista) 
lista = [x for x in range(4) if x%2 == 0] #keeps only even numbers

## practise questions loops

# Q1 — Print numbers from 1 to 10


# Q2 — Print all even numbers from 1 to 20


# Q3 — Print numbers from 10 to 1


# Q4 — Find the sum of numbers from 1 to 100


# Q5 — Given this list, print every item:

numbers = [10, 20, 30, 40, 50]


# Q6 — Given this list, print only even numbers:

numbers = [12, 7, 9, 20, 15, 8, 3]


# Q7 — Count how many even numbers are in this list:

numbers = [12, 7, 9, 20, 15, 8, 3]


# Q8 — Find the largest number WITHOUT using max():

numbers = [12, 45, 7, 89, 23, 56]


# Q9 — Find the sum of all numbers in this list WITHOUT using sum():

numbers = [12, 45, 7, 89, 23]


# Q10 — Print every character in this string:

text = "Bhargav"


# Q11 — Count how many vowels are in this string:

text = "Programming"


# Q12 — Print numbers from 1 to 20, but skip multiples of 3 using continue


# Q13 — Print numbers from 1 onwards and stop when you reach 7 using break


# Q14 — Search for a number in this list.
# Print "Found" and stop the loop if the number is found.
# Otherwise print "Not Found".

numbers = [10, 25, 30, 45, 50]
target = 30


# Q15 — Print this pattern:

# *
# **
# ***
# ****
# *****


## Practice questions for list comprehension 

# Q1 — Create a list containing numbers from 0 to 9


# Q2 — Create a list containing squares of numbers from 1 to 10

# Expected:
# [1, 4, 9, 16, ...]


# Q3 — Create a list containing only even numbers from 0 to 20


# Q4 — Given this list, create a new list containing the squares:

numbers = [1, 2, 3, 4, 5]

# Expected:
# [1, 4, 9, 16, 25]


# Q5 — Given this list, create a new list containing only even numbers:

numbers = [10, 15, 20, 25, 30, 35]


# Q6 — Convert every string in this list to uppercase:

names = ["bhargav", "python", "coding"]


# Q7 — Get the length of every word:

words = ["apple", "banana", "cat", "programming"]



# Q8 — Create all possible pairs using nested list comprehension:

list1 = [1, 2]
list2 = ["a", "b"]

# Expected:
# [(1, "a"), (1, "b"), (2, "a"), (2, "b")]