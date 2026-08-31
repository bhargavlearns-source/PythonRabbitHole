#In python variables are the name which are reffering to an object, but two variable can also reffer to a same object.

a = 10
b = a
print(a is b) #This will print True because a and b are technically reffering to the same object in the memory space
print(a == b) #This checks that a and b have equal values
a = "hello world"
b = a
print(a is b) #This will be true here
b.capitalize() #Strings are immutable which means this will return a new string 
#with capitalize initial but in order to make use of it we need to assign it to a variable name
b = b.capitalize() #This will generate a new string
print(a, b)
print(a is b) #this will be false

#in case of lists things are messy, because list is a mutable object in python.
#it means that we can change the original list using python build in functions for list.

L1 = [1,2,3]
L2 = L1
print(L1 is L2) #True because they share same memory location
L1.append(4) #remember this will append 4 in the L1 list but it will return None
# L1 = L1.append(4)
# print(L1) #This will return None if we try to do it!

#Now if we print L1 and L2:
print("L1:",L1,"","L2:",L2) #Remember print can take as many inputs as you want
#Both lists will be converted to [1,2,3,4], this is because they share the same list techincally.

#Now in order to make two seperate list you can do this following:
L1 = [1,2,3]
L2 = L1[:] #[1,2,3]
print(L1 is L2) #False because now L1 and L2 are two different lists
print("L1:",L1,"","L2:",L2)
#Now if you do:
L2.append(4)
print("L1:",L1,"","L2:",L2) 
#L1 will be [1,2,3] L2 will be [4,5,6]

#Another method (copy vs deepcopying)
L1 = [1,2,3]
L2 = L1.copy() #This will create a shallow copy of L1 in memory and refer it to L2
print(L1 is L2) 
print("L1:",L1,"","L2:",L2)
#However, if L1 is a nested list then things will work differently
L1 = [[1,2], [3,4]]
L2 = L1.copy()
print(L1 is L2) #This will print false
print("L1:",L1,"","L2:",L2)
print(L1[0] is L2[0]) #This will print true because the internal list elements are same in both the list
#This means
L1[0].append(100)
print(L1 is L2) #This will still be false
print("L1:",L1,"","L2:",L2) 
#L1: [[1, 2, 100], [3, 4]]  L2: [[1, 2, 100], [3, 4]] this will be the outcome
#Hence there is a final way to do this!

import copy #Copy is a module in python, you can import modules in your python file which contains set of intructions!

L1 = [[1,2], [3,4]]
L2 = copy.deepcopy(L1)
print(L1 is L2) #False 
print(L1[0] is L2[0]) #This will be false too
#This is called deep copying and it is a great way to copy a list.

#Practice questions

# ============================================================
# PREDICT THE OUTPUT — REFERENCES, COPY & DEEPCOPY
# ============================================================


# ============================================================
# Q1. Normal Assignment
# ============================================================

L1 = [1, 2, 3]
L2 = L1

L2.append(4)

print(L1)
print(L2)
print(L1 is L2)


# ============================================================
# Q2. Shallow Copy (Simple List)
# ============================================================

L1 = [1, 2, 3]
L2 = L1.copy()

L2.append(4)

print(L1)
print(L2)
print(L1 is L2)


# ============================================================
# Q3. Shallow Copy With Nested Lists
# ============================================================

L1 = [[1, 2], [3, 4]]
L2 = L1.copy()

L2[0].append(100)

print(L1)
print(L2)
print(L1[0] is L2[0])


# ============================================================
# Q4. Replacing vs Modifying
# ============================================================

L1 = [[1, 2], [3, 4]]
L2 = L1.copy()

L2[0] = [100, 200]

print(L1)
print(L2)
print(L1[0] is L2[0])


# ============================================================
# Q5. Deep Copy
# ============================================================

import copy

L1 = [[1, 2], [3, 4]]
L2 = copy.deepcopy(L1)

L2[0].append(100)

print(L1)
print(L2)
print(L1[0] is L2[0])


# ============================================================
# Q6. The Famous Matrix Trap
# ============================================================

matrix = [[0] * 3] * 3

matrix[0][1] = 99

print(matrix)


# ============================================================
# Q7. The Correct Matrix Creation
# ============================================================

matrix = [[0] * 3 for _ in range(3)]

matrix[0][1] = 99

print(matrix)


# ============================================================
# Q8. == vs is
# ============================================================

L1 = [[1, 2], [3, 4]]
L2 = L1.copy()

print(L1 == L2)
print(L1 is L2)

print(L1[0] == L2[0])
print(L1[0] is L2[0])


# ============================================================
# Q9. List Repetition
# ============================================================

L = [1, 2]

result = [L] * 3

result[1].append(99)

print(result)
print(result[0] is result[2])


# ============================================================
# Q10. FINAL BOSS
# ============================================================

import copy

L1 = [[1, 2], [3, 4]]

L2 = L1.copy()
L3 = copy.deepcopy(L1)

L1[0].append(99)
L2[1] = [100]

print("L1:", L1)
print("L2:", L2)
print("L3:", L3)


# ============================================================
# RULE:
# Predict the output BEFORE running the code 😈
# ============================================================
