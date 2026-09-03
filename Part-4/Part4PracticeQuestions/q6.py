def create_counter():
    count = 0
    def increment():
        nonlocal count
        count +=1
        return count
    return increment # Do you know why we didnt use increment() or return increment() here?

# Returning increment will do something magical here

counter1 = create_counter() # create_counter() on calling, return increment. This means now counter1 is binded with the increment function.

print(counter1())   # 1 because we are techinally calling increment becasue counter1 is increment only
print(counter1())   # 2 because we called it twice
print(counter1())   # 3 same reason

# You have literally discovered major part of the decorators, which is one of the hardest concepts in python to learn.
