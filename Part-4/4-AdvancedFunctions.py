#Recursion:
#It is a function which calls itself!

def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1) # Here factorial is calling the function again and again

#I still recommend watching a dedicated video for learning recursion.


#Functions are objects btw, which means you can pass them in other functions, in lists or assign them to variables.

def hello():
    print("Hello")

x = hello # Now it is easy for you to guess, hello and x are bind to same function object in memory space.
x() #This will call the function object which binds with hello variable

## Lambda

double = lambda x: x*2 # This returns double of x, when we call double.

print(double(5))

## map

lista = [1,2,3]

doublelist = map(lambda x: x*2,lista) #This will create a map object
print(list(doublelist)) # We always have to convert the map object to list or tuple or any preferable data type to get your result

# filter

nums = [1, 2, 3, 4, 5]

result = filter(lambda x: x % 2 == 0, nums)

print(list(result))

# Generator

# Generator is used for saving memory, it yield one value at a time and it require next() to call the next value

def test():
    yield 1
    yield 2
    yield 3

g = test()

print(next(g))
print(next(g))
print(next(g))
# print(next(g)) This will raise stop iteration error

for i in test(): #You can use for loop as well
    print(i)

# generator comprehension

gen = (x for x in range(10))
print(gen) #This will print gen object
print(list(gen)) #This will print list
