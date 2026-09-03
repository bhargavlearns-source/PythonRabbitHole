#When you do print(x), python does a search operation!
"""
It searches in this order:

L → Local

Current function.

E → Enclosing (only if we have nested functions)

Outer function(s).

G → Global

The current module/file.

B → Built-in

Python's built-in names.
"""

# Local:
x = 100
def test():
    x=10
    print(x)

test() #10 will be print because python will prioritise local.

# Enclosing:

x = 100
def outer():
    x = 20
    def inner():
        print(x) #There is no x in local this time so it will have to use the value present in the enclosing function
    inner()

outer()
# inner() #You can not call this because it is parto of outer namespace not global namespace

#Global 

x = 100

def test():
    print(x)

test() #This will print x

# Build in functions:
print(len([1,2,3])) # You never define len, however python still used it!
# this is because when it doesnt find anything in local, enclosing and global namespace it find in python build in function list

# But uk what? 
# There is a catch.

x = 100

def test():
    x = x+10
    print(x)

# test() guess the outcome!
# This will raise an error, because when we use assignment inside a function it consider x part of the local namespace but there is no x over there.

# But what if i pass x?
x = 100
def test(x):
    x = x+10
    print(x)

test(x) #Guess the outcome again! 
# This time it will be 110, because x is available in python local namespace!
print(x) #Guess the outcome?
# This will be 100, because python creates local namespace but it doesnt effect the global namespace.

# But there are ways to manipulate the global x using python functions and built in keywords.

## Global

x = 10

def test():
    global x #Now the x is reffering to the x in the global namespace.
    x = 20

test()

print(x)

## Non local
def outer():
    x = 10
    print(x)
    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()

# ==========================================
# PYTHON SCOPES — PREDICT THE OUTPUT
# LEGB | Local | Enclosing | Global | Built-in
# ==========================================


# ==========================================
# Q1 — Local vs Global
# ==========================================

x = 10

def test():
    x = 20
    print(x)

test()
print(x)


# ==========================================
# Q2 — Global Lookup
# ==========================================

x = "Global"

def test():
    print(x)

test()


# ==========================================
# Q3 — Local Beats Global
# ==========================================

x = "Global"

def test():
    x = "Local"
    print(x)

test()
print(x)


# ==========================================
# Q4 — Enclosing Scope
# ==========================================

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        print(x)

    inner()

outer()


# ==========================================
# Q5 — Local Beats Enclosing
# ==========================================

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()
    print(x)

outer()


# ==========================================
# Q6 — Enclosing Beats Global
# ==========================================

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        print(x)

    inner()

outer()


# ==========================================
# Q7 — global Keyword
# ==========================================

x = 10

def change():
    global x
    x = 50

change()

print(x)


# ==========================================
# Q8 — nonlocal Keyword
# ==========================================

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()


# ==========================================
# Q9 — Nested Scope Lookup
# ==========================================

x = "Global"

def outer():
    x = "Outer"

    def middle():
        x = "Middle"

        def inner():
            print(x)

        inner()

    middle()

outer()


# ==========================================
# Q10 — Tricky LEGB 😈
# ==========================================

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        print(x)

    inner()

    x = "Changed Enclosing"

    inner()

outer()

print(x)