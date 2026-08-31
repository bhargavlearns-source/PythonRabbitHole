'''
Polymorphism sounds scary but it is not!
'''
#Plymorphism is a greek word which means many forms.
#Polymorphism allows user to use same operator on different objects, which may result in different result.

a = 10
b = 10
print(a+b) #Here a + b will be added manually
a = "bhargav"
b = "Mahajan"
print(a+b) #Here a + b will return a concatenated string

#In addition to this knowledge while taking inputs in python the object which is created contains string.
#Due to this we need to change the object type while taking inputs according to our needs

name = input("Enter your name:") #This will take an input and returns a string.
age = input("Enter your age:") #This will take an input and returns a string but we want int.
print("Type of name:", type(name),"Type of age:", type(age)) #Output: Type of name: <class 'str'> Type of age: <class 'str'>

#In order to convert this, we use int(input("Enter your age:"))
age = int(input("Enter your age:"))
print("Type of age:", type(age))

#The main point of this chapter was two objects can work differently using the same operator but two different objects do not work using the same operator.
#practice questions!!!
#Q1: Explain polymorphism into your own words.
#Q2: Write a program which take an input from user, you can take any input you want.
#Q3: Try experimenting with other data types like list + list, dictionary + dictionary and note your results.
