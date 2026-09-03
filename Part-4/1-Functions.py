## Why do we need functions?

name = "Bhargav"
print(f"Hello {name}")

name = "Paru"
print(f"Hello {name}")

name = "Rahul"
print(f"Hello {name}")

#this will work but how long you will keep writing this?
#However the better way to do it will be:

def greet(name):
    print(f"hello {name}")

greet("Bhargav") #this will print hello Bhargav

# Now in python the more tools you learn, the more complex programs you can write with them.
# However, in reality the more tools you use, the less number of lines it will take you to write a code.
# In short in python, you learn things to make your code more readable and make it more efficient.

# Now what is happening internally??

# def is an executable statement.
print("HI")
def hello():
    print("hello")
print("BYE")

# Python line by line execute its program.
# Firstly it will execute the print statement and print HI
# Then python will execute def statement and creates a function object and binds it with the name hello.
# when we will call the hello, it will line by line start to execute the function body.
# Lastly BYE will print!

def test():
    x=10
    print(x)

test() #10 will be print
# print(x) this will raise an error, do you know why?
# This is because the x is part of python function object's namespace.
# so we cant call it globaly

# Infact the arguements we pass also becomes local variable
def greet(name):
    #Python automatically does name = bhargav (if we pass bhargav) in the local namespace of greet
    print(name)
greet("Bhargav")


#Python functions are polymorphic
def double(x):
    print(x*2)

double("hi") #it will print hihi
double(2) #it will print 4

