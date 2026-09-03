# Python uses pass by assignment (I never understood that myself but lets understand the actual meaning)

def change(x):
    print(x is a) #This means x and a are binded to same object.
    x = 100

a = 10
change(a) # Now if a and x are same in memory space this should make it 100
print(a)

# This is a big gotcha in python but we have kind off understood this in our previous file (Scopes.py).
# When we call a function with arguement, the arguements which have passed and arguements in the functions reffer to same object.
# But when we did x = 100, we simply assgined x to a different object!
# so thats why when we print a outside the function it stays the same.
# The main reason why this happens is because the object which we are using for this example is immutable.

# Now if the object is mutable:

def change(x):
    # print(x is a)
    x.append(100) 
    # a.append(1000)
    # Both will work because here also Lgeb rule will apply
    # keep one thing in your memory, only when we use assignment in functions then only python creates or find local variable, else it will follow lgeb rule.
    # a = [100,200] #The moment you run this, python will raise an error because now a is a local variable.
    # a.append(100)
    x = [100] #This will make x binds to a new list
a = [1,2,3,4,]
print(a)
change(a) # Now if a and x are same in memory space this should make it 100
print(a)

## Postitional arguements

def greet(name):
    print(name)

greet("Bhargav") #Here "Bhargav" is a postional arguement

## Keyword arguement

def greet(name,age):
    print(f"{name}:{age}")

greet(age = 19, name = "bhargav") #Here we can assign arguements in any order

## Default arguement
def greet(name="Guest"):
    print("Hello", name)

greet()


# *args and **kwargs (You will thank me later for putting this topic in this file)

def greet(name,milk, extra):
    print(f"\nName: {name}\nMilk: {milk}\nExtra: {extra}") #This will work for 1 extra

greet("Bhargav", "Oat milk", "Whipped cream") #This will print the name, the milk and the extra

# But what if the extra will be more than 1.
# For that we use args

def greet(name, milk, *extra):
    print(f"\nName: {name}\nMilk: {milk}") 
    print("Extra:")
    print(extra) #This will print a tuple
    print(type(extra)) #This verify that
    for i in extra:
        print(i)

greet("Bhargav", "Oat milk", "Whipped cream", "Chocolate", "Gems")
# *args collects postional arguements into a tuple

nums = [1, 2, 3]

print(*nums) # This is equvivalent to print(1,2,3) 

#** kwargs are similar to *args but it stores a dictionary

def test(**kwargs):
    print(kwargs)
    print(type(kwargs))

test(name="Bhargav", age=19)

#Multiple return values
def test():
    return 10, 20

a,b = test() # test() returns a tuple
print(a,b)




