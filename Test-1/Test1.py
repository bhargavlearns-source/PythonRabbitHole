"""
=============================================================
PYTHON MODERATE-LEVEL TEST — Chapters 1-21 (Learning Python)
=============================================================
Topics covered: interpreter/execution model, core object types,
mutability/assignment, truth testing, statements & loops,
comprehensions, functions, scope (LEGB), nonlocal/global,
CLOSURES (extra weight, per request), lambda/map/filter/sorted.

HOW TO TAKE THIS TEST
----------------------
1. Do NOT run this file for the answers — work it out on paper/in
   your head first, then verify by running snippets if you want.
2. Write your answers in a Google Doc / Word doc, numbered to
   match the question numbers below (e.g. "A1: b", "B3: [0, 4, 16]",
   "C2: bug is on line X, fix is ...", "D1: <your code>").
3. When done, copy your answer doc's content and use the
   ASSESSMENT PROMPT at the very bottom of this file — paste it
   into any AI model along with your answers, and ask it to grade
   you and explain anything you got wrong.

Time suggestion: ~50-60 minutes. Closed book if you want a real
gauge of where you stand.
=============================================================
"""

# =============================================================
# SECTION A — MULTIPLE CHOICE (10 questions, 1 mark each)
# =============================================================

# A1. What does the Python interpreter produce after tokenizing
#     and parsing your source code, before it runs on the PVM?
#     a) Machine code
#     b) Byte code
#     c) An executable binary
#     d) An abstract syntax tree only, nothing further

# A2. Which of these is an IMMUTABLE type?
#     a) list
#     b) dict
#     c) tuple
#     d) set

# A3. What is printed?
#     print(type([]) == type(list()))
#     a) True
#     b) False
#     c) Error
#     d) None

# A4. Which statement correctly describes Python variable assignment?
#     a) Variables are boxes that store values directly
#     b) Names are labels bound to objects in memory
#     c) Assignment always creates a copy of the right-hand value
#     d) Variables must be declared with a type before assignment

# A5. What does `and` return in Python (not a boolean language)?
#     a) Always True or False
#     b) The first operand if it's falsy, otherwise the second operand
#     c) The second operand if it's falsy, otherwise the first operand
#     d) 1 or 0

# A6. Which of the following is considered FALSE in a boolean context?
#     a) [0]
#     b) "False"
#     c) {}
#     d) -1

# A7. What does the `nonlocal` keyword do?
#     a) Declares a variable as global
#     b) Lets an inner function assign to a name in its enclosing
#        (non-global) scope
#     c) Deletes a variable from the local scope
#     d) Makes a variable accessible outside the module

# A8. In LEGB scope resolution order, what does the "E" stand for?
#     a) External
#     b) Environment
#     c) Enclosing
#     d) Exception

# A9. What is a closure?
#     a) A function that has no arguments
#     b) A function object that remembers values from its enclosing
#        lexical scope, even after that scope has finished executing
#     c) A statement that closes a file automatically
#     d) A loop that never terminates

# A10. What does `iter(iterable)` return?
#      a) The first item of the iterable
#      b) An iterator object that supports __next__()
#      c) A list copy of the iterable
#      d) A generator function


# =============================================================
# SECTION B — PREDICT THE OUTPUT (8 questions, 2 marks each)
# =============================================================

# B1.
# x = (1, 2, 3)
# y = x
# print(x is y)

# B2.
# d = {'a': 1}
# e = d.copy()
# e['b'] = 2
# print(d)

# B3.
# nums = [1, 2, 3, 4, 5]
# result = [n * 2 for n in nums if n % 2 != 0]
# print(result)

# B4.
# print(bool(''), bool(' '), bool([]), bool([0]))

# B5.  -- CLOSURE FOCUS --
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
#
# c1 = make_counter()
# c2 = make_counter()
# print(c1(), c1(), c2())

# B6.  -- CLOSURE FOCUS --
# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)
# print([f() for f in funcs])

# B7.  -- CLOSURE FOCUS --
# funcs = []
# for i in range(3):
#     funcs.append(lambda i=i: i)
# print([f() for f in funcs])

# B8.
# def outer():
#     x = 5
#     def inner():
#         print(x)
#         x = 10
#     inner()
# outer()


# =============================================================
# SECTION C — FIND THE BUG (5 questions, 2 marks each)
# Each snippet has exactly one bug. State the bug AND the fix.
# =============================================================

# C1.
# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list
#
# print(add_item(1))
# print(add_item(2))
# # Bug: what will the SECOND call print, and why is that probably
# # not what the programmer intended? How would you fix it?

# C2.
# def make_multiplier(n):
#     def multiply(x):
#         return x * n
#     n = n * 10   # <-- something's off here
#     return multiply
#
# times5 = make_multiplier(5)
# print(times5(2))
# # Bug: what value does this actually print, and why might it
# # surprise someone who expects times5(2) == 10?

# C3.
# total = 0
# for i in range(5):
#     total = total + i
#     if total > 5:
#         break
# else:
#     print("Loop finished without breaking")
# print(total)
# # Bug: is there actually a bug? Explain what the for/else does here.
# # (Trick question — but explain WHY the else did or didn't run.)

# C4.
# def get_value(d, key):
#     if key in d:
#         value = d[key]
#     return value
#
# print(get_value({'a': 1}, 'b'))
# # Bug: what error occurs, and why? Fix it.

# C5.
# class Counter:
#     count = 0
#     def increment(self):
#         count = count + 1
#         return count
#
# c = Counter()
# print(c.increment())
# # Bug: what error occurs? Fix it (hint: think about namespaces).


# =============================================================
# SECTION D — PURE QUESTION SOLVING (7 questions, 3 marks each)
# Write actual working code for each.
# =============================================================

# D1. Write a list comprehension that returns the squares of all
#     numbers from 1 to 20 that are divisible by 3.

# D2. Write a function `make_power(exp)` that returns a closure
#     which, when called with a number x, returns x raised to exp.
#     (e.g. square = make_power(2); square(5) == 25)

# D3. Write a function `running_total()` that returns a closure with
#     no arguments; each call to that closure should return the sum
#     of ALL numbers passed to it so far via an internal counter that
#     increases by 1 each call (i.e. call 1 returns 1, call 2 returns
#     3, call 3 returns 6, etc. — like a running total of 1+2+3...).

# D4. Using `sorted()` with a `key=` lambda, sort this list of tuples
#     by the second element in descending order:
#     data = [('a', 3), ('b', 1), ('c', 2)]

# D5. Write a generator function `countdown(n)` that yields numbers
#     from n down to 1, then stops (no explicit StopIteration needed).

# D6. Using `map()` and `filter()` (not comprehensions), produce a
#     list of the cubes of all even numbers from this list:
#     nums = [1, 2, 3, 4, 5, 6, 7, 8]

# D7. Write a function `make_accumulator()` that returns a closure
#     `add(x)`. Each call to add(x) should add x to a running total
#     stored in the enclosing scope and return the new total.
#     (e.g. acc = make_accumulator(); acc(10) -> 10; acc(5) -> 15)


# =============================================================
# END OF TEST
# =============================================================


"""
=============================================================
ASSESSMENT PROMPT — paste this + your answers into any AI model
=============================================================

I just took a moderate-level Python test covering chapters 1-21
of "Learning Python" by Mark Lutz (interpreter/execution model,
core object types, mutability, truth testing, statements/loops,
comprehensions, functions, scope/LEGB, nonlocal/global, closures,
lambda/map/filter/sorted).

The test has 4 sections:
- Section A: 10 MCQs (1 mark each)
- Section B: 8 Predict-the-Output questions (2 marks each)
- Section C: 5 Find-the-Bug questions (2 marks each)
- Section D: 7 Pure code-writing questions (3 marks each)
Total: 57 marks.

Below are my answers. Please:
1. Grade each answer as correct/incorrect/partial, with the mark
   awarded out of the total for that question.
2. For anything incorrect or partial, explain clearly WHY, and
   correct my misunderstanding — don't just give the right answer,
   help me understand the underlying concept.
3. Give me a total score out of 65 and a percentage.
4. Flag if I seem weak in any particular topic area (e.g. closures,
   scope, mutability) based on the pattern of mistakes, so I know
   what to revise before moving on.

Here are my answers:

[PASTE YOUR ANSWERS HERE, e.g.:
A1: b
A2: c
...
B1: True
...
C1: bug is ..., fix is ...
...
D1:
squares = [x**2 for x in range(1, 21) if x % 3 == 0]
...
]
=============================================================
"""