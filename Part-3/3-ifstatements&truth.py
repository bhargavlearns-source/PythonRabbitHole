#if else basic syntax

age = 19

if age>= 18:
    print("Valid age")

else:
    print("Invalid age")

# if/elif/else ladder

marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

#inline else if
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

#better way to solve this:
status = "adult" if age>=18 else "minor" #valid_if_true if condition else valid_if_false
print(status)

#in python all these values below are false:

'''
False
None
0
0.0
""
[]
{}
()
set()
'''

#This means:
if ():
    print("Empty")
else:
    print("false")

# or & and operator

#this now will change your mind, or & and never worked like you imagined it to work:

#or :- If the fist operand is false return second operand else return first
print(0 or 10) #here 0 is the first operand which means this should return 10
print(10 or 5) #here first operand was true hence it return it 

#and :- If the first operand is false return first operand or else second

print(0 and 10) #this will print 0
print(10 and 0) #this will again return 0 because first operand is true
print(10 and 20) #this will return 20

#Take your time man, digest this info!

### Practice questions ###
# Q1 — Positive, Negative, or Zero
num = -7

# Print: Positive, Negative, or Zero


# Q2 — Largest of Three
a = 10
b = 25
c = 15

# Print the largest number without using max()


# Q3 — Even or Odd
num = 17

# Print: Even or Odd


# Q4 — Grade Calculator
marks = 72

# 90+ → A
# 75–89 → B
# 60–74 → C
# 40–59 → D
# Below 40 → Fail


# Q5 — Leap Year
year = 2024

# A year is a leap year if:
# Divisible by 400
# OR divisible by 4 but NOT divisible by 100

# Print: Leap Year or Not a Leap Year


# Q6 — Password Check
password = "python123"

# If password is "admin" → Access Denied
# If password length is less than 8 → Password too short
# Otherwise → Access Granted


# Q7 — Triangle Type
a = 5
b = 5
c = 8

# Equilateral → all sides equal
# Isosceles → exactly two sides equal
# Scalene → all sides different


# Q8 — Predict the Output (don't run it first)
x = 10

if x > 5:
    print("A")

if x > 8:
    print("B")

else:
    print("C")

#Q9: Try researching on how python executes if statements. (it's simple though)