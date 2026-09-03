def add_bonus(numbers, bonus):
    global result
    result = []
    for i in numbers:
        result.append(i+bonus)
    return result

numbers = [10,20,30]
add_bonus(numbers,5)
print(result)
numbers = [10, 20, 30]
add_bonus(numbers, 33)
print(result)