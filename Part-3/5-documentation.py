# CHAPTER 15 — THE DOCUMENTATION INTERLUDE (Just give it a read nothing much)

# 1. COMMENTS (#)
# ----------------

# Comments are notes written for humans reading the code.

# Example:

# # This calculates the total price
# total = price * quantity

# Python ignores comments during execution.

# Use comments for small explanations or important notes.


# 2. DOCSTRINGS
# -------------

# Docstrings are used to document larger pieces of code such as:

# - Modules
# - Functions
# - Classes
# - Methods

# Example:

# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b

# A docstring can be accessed using:

# print(add.__doc__)


# 3. __doc__
# ----------

# The __doc__ attribute stores an object's docstring.

# Example:

# def greet():
#     """This function prints a greeting."""
#     print("Hello")

# print(greet.__doc__)


# 4. dir()
# --------

# dir() shows the attributes and methods that can be accessed on an object.

# Example:

# x = []

# print(dir(x))

# This will show things like:

# append
# pop
# remove
# sort

# Mental model:

# dir(object)

# = "What attributes can I access on this object?"


# 5. __dict__
# -----------

# __dict__ shows the namespace dictionary directly stored on an object.

# Example:

# class Person:
#     species = "Human"

# print(Person.__dict__)

# Mental model:

# __dict__

# = "What attributes are directly stored in this object's namespace?"


# IMPORTANT DIFFERENCE:

# dir(obj)
# → Shows attributes that can be accessed, including inherited attributes.

# obj.__dict__
# → Shows attributes directly stored in that object's namespace.


# 6. help()
# ---------

# help() displays documentation about an object.

# Examples:

# help(str)

# help(list)

# help(print)

# help(str.upper)

# It uses Python's documentation system and docstrings.


# 7. PYDOC
# --------

# PyDoc is Python's documentation system.

# It uses:

# - Docstrings
# - Module information
# - Classes
# - Functions
# - Methods

# PyDoc powers:

# help()

# It can also generate documentation pages for Python code.


# FINAL MENTAL MAP
# ----------------

# Documentation:

# # comments
#     ↓
# Small notes for humans

# """docstrings"""
#     ↓
# Documentation for modules, functions, classes, and methods

# __doc__
#     ↓
# Access an object's docstring

# dir()
#     ↓
# See accessible attributes

# __dict__
#     ↓
# See directly stored namespace

# help()
#     ↓
# Read documentation about an object

# PyDoc
#     ↓
# Python's documentation system