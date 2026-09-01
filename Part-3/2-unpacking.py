#we studied about tuple and even added unpacking questions intentionally in the practice sheets but here is something subtle.
#In python we can use * for taking postional arguements and it is very important to know because later on we will use this in functions.

a = 10 #normal assignment
a = b = c = 10 #multiple assignment (here a is b, a is c and b is c, which means in memory all these variables are associtated with same object)
print(a is b)

a,b = [10,20]
print(a,b) #a will be assign to 10 and b will be assigned to 20

a,*b = (1,2,3,4,5,5,5) #*b will take all the numbers after a takes the first elements into a list
print(a)
print(b)
print(type(a), type(b))

a = 9
b = 4
#augmented assignment 
a += 10 #this means a = a + 4 (this is more python way of writing code)
b -= 30 # b = b - 30
a/= 4 # a = a/4 (this returns float)
print(a, type(a))

#print customization
print(f"hello world {a}") #we have used this many times
print("hello", "world", sep= "-") #this creates hello-world
print("hello", "world", end= " ") #this removes the newline which python gives 
print("hi") 
