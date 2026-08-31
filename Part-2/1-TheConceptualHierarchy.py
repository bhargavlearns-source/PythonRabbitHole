'''The python programs contains modules,
modules contains statements, statements contains expressions
expressions contains objects'''

#A simple code of adding two numbers
def add(a,b):
    return a+b

print(add(5,5))

#A modules is a basically a python file (ex: hello.py, main.py, etc)
#A module is simply a namespace.
#Namespace is a place which contains the name of the objects.
#Here in this example we are using TheConceptualHierarchy.py module
#Now this TheConceptualHierarchy.py contains def statement.
#This def statement is executable statement, which means it creates a temporary namespace.
#After creating a temporary namespace it executes the function line by line.
#The statements itself contains statements which holds expressions like a+b
#this expressions later process and create an object.
#However when the functions finish executing, it will create an function object in the module namespace.

#In short python is an object oriented language!

# Practice questions!!!
# Q1: If every program contains module then how we are able to write program in a module?
# Q2: If namespace is a place which contains names along with their objects, then everything in python is part of the namespace or not?