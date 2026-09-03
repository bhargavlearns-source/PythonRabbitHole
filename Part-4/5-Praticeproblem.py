# ============================================================
# PART IV — FUNCTIONS PRACTICE
# Difficulty: Moderate
# Topics: Functions, Scope, Arguments, Closures, Recursion,
#         Lambda, Comprehensions & Generators
# ============================================================


# ============================================================
# Q1 — Custom Power Function
# ============================================================
#
# Create a function called power() that accepts:
#
# - a number
# - an optional power value (default = 2)
#
# Return the number raised to that power.
#
# Examples:
#
# power(5)       -> 25
# power(2, 3)    -> 8
# power(10, 1)   -> 10
#
# Do not use ** operator.
#
# ============================================================


# ============================================================
# Q2 — Flexible Average
# ============================================================
#
# Create a function average(*args).
#
# It should accept any number of numerical arguments and
# return their average.
#
# Examples:
#
# average(10, 20, 30)       -> 20
# average(5, 10)            -> 7.5
# average(1, 2, 3, 4, 5)    -> 3
#
# Handle the case where no arguments are passed.
#
# ============================================================


# ============================================================
# Q3 — Student Information
# ============================================================
#
# Create a function student_info(name, age, **kwargs).
#
# Print the name and age normally.
#
# Then print all additional information passed through kwargs.
#
# Example:
#
# student_info(
#     "Bhargav",
#     19,
#     city="Gurdaspur",
#     course="CSE",
#     hobby="Programming"
# )
#
# ============================================================


# ============================================================
# Q4 — Modify or Copy?
# ============================================================
#
# Create a function add_bonus(numbers, bonus).
#
# The function should add the bonus to every number.
#
# IMPORTANT:
#
# Do NOT modify the original list.
#
# Return a NEW list instead.
#
# Example:
#
# numbers = [10, 20, 30]
#
# result = add_bonus(numbers, 5)
#
# result  -> [15, 25, 35]
# numbers -> [10, 20, 30]
#
# ============================================================


# ============================================================
# Q5 — Scope Challenge
# ============================================================
#
# Create a global variable:
#
# score = 0
#
# Create a function called update_score(points).
#
# It should update the GLOBAL score by adding points.
#
# Example:
#
# update_score(10)
# update_score(20)
#
# print(score)
#
# Expected:
#
# 30
#
# ============================================================


# ============================================================
# Q6 — Counter Closure
# ============================================================
#
# Create a function called create_counter().
#
# Inside it:
#
# - Create a variable count = 0
# - Create an inner function increment()
# - Every time increment() is called, count should increase by 1
# - Return the increment function
#
# Example:
#
# counter1 = create_counter()
#
# print(counter1())   # 1
# print(counter1())   # 2
# print(counter1())   # 3
#
# counter2 = create_counter()
#
# print(counter2())   # 1
#
# Each counter should have its OWN state.
#
# ============================================================


# ============================================================
# Q7 — Recursive Sum
# ============================================================
#
# Write a recursive function recursive_sum(n).
#
# It should calculate:
#
# 1 + 2 + 3 + ... + n
#
# Example:
#
# recursive_sum(5)
#
# 1 + 2 + 3 + 4 + 5
#
# Output:
#
# 15
#
# Do not use loops.
#
# ============================================================


# ============================================================
# Q8 — Function as an Argument
# ============================================================
#
# Create these functions:
#
# square(x)
# cube(x)
#
# Then create another function:
#
# apply_operation(numbers, operation)
#
# It should apply the given function to every number in the list
# and return a new list.
#
# Example:
#
# numbers = [1, 2, 3]
#
# apply_operation(numbers, square)
#
# Output:
#
# [1, 4, 9]
#
# apply_operation(numbers, cube)
#
# Output:
#
# [1, 8, 27]
#
# ============================================================


# ============================================================
# Q9 — Dictionary Comprehension
# ============================================================
#
# Given:
#
# words = ["python", "java", "c", "javascript"]
#
# Create a dictionary where:
#
# key   = word
# value = length of word
#
# Expected:
#
# {
#     "python": 6,
#     "java": 4,
#     "c": 1,
#     "javascript": 10
# }
#
# Use a dictionary comprehension.
#
# ============================================================


# ============================================================
# Q10 — Generator: Even Numbers
# ============================================================
#
# Create a generator function even_numbers(n).
#
# It should generate all even numbers from 0 up to n.
#
# Example:
#
# g = even_numbers(10)
#
# print(list(g))
#
# Output:
#
# [0, 2, 4, 6, 8, 10]
#
# Use yield.
#
# ============================================================


# ============================================================
# Q11 — Generator Pipeline 😈
# ============================================================
#
# Create a generator function called squares(numbers).
#
# It should receive an iterable of numbers and yield the square
# of each number ONE AT A TIME.
#
# Example:
#
# nums = [1, 2, 3, 4]
#
# g = squares(nums)
#
# print(next(g))   # 1
# print(next(g))   # 4
#
# Then convert the remaining values into a list.
#
# Expected remaining:
#
# [9, 16]
#
# ============================================================


# ============================================================
# Q12 — Keyword-Only Arguments
# ============================================================
#
# Create a function:
#
# create_profile(name, *, age, city)
#
# age and city MUST be keyword-only arguments.
#
# Example:
#
# create_profile(
#     "Bhargav",
#     age=19,
#     city="Gurdaspur"
# )
#
# Print the profile nicely.
#
# Try calling it incorrectly too and observe the error.
#
# ============================================================


# ============================================================
# Q13 — Lambda + Sorting
# ============================================================
#
# Given:
#
# students = [
#     ("Bhargav", 85),
#     ("Paru", 92),
#     ("Rahul", 78),
#     ("Aman", 88)
# ]
#
# Sort the students according to their marks.
#
# Use:
#
# - sorted()
# - lambda
#
# Sort from highest marks to lowest marks.
#
# ============================================================


# ============================================================
# Q14 — Closure with Custom Multiplier
# ============================================================
#
# Create a function:
#
# create_multiplier(n)
#
# It should return another function that multiplies its input
# by n.
#
# Example:
#
# double = create_multiplier(2)
# triple = create_multiplier(3)
#
# print(double(10))   # 20
# print(triple(10))   # 30
#
# IMPORTANT:
#
# Understand WHY both functions remember different values of n.
#
# ============================================================


# ============================================================
# Q15 — The Final Moderate Challenge 😈
# ============================================================
#
# Create a function called process_numbers(numbers, operation).
#
# Requirements:
#
# 1. numbers is a list of integers.
#
# 2. operation is a function.
#
# 3. Apply operation to every number.
#
# 4. Only keep results greater than 10.
#
# 5. Return the final results as a list.
#
# Example:
#
# numbers = [1, 2, 3, 4, 5]
#
# process_numbers(numbers, lambda x: x * 3)
#
# Step 1:
#
# [3, 6, 9, 12, 15]
#
# Step 2 — Keep values > 10:
#
# [12, 15]
#
# Final Output:
#
# [12, 15]
#
# Try solving this first with normal loops.
#
# Then try solving it using comprehensions.
#
# ============================================================

