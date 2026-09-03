def square(num):
    return num **2

def cube(num):
    return num **3

def apply_operation(numbers, operation):
    result = []
    for i in numbers:
        j = operation(i)
        result.append(j)
    return result


numbers = [1, 2, 3]

print(apply_operation(numbers, square))

# Output:
# [1, 4, 9]

print(apply_operation(numbers, cube))

# Output:
# [1, 8, 27]

