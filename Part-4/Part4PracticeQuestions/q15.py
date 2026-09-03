def process_numbers(numbers, fun = None):
    result = map(fun, numbers)
    newresult = []
    for i in list(result):
        if i>10:
            newresult.append(i)
    return newresult

numbers = [1, 2, 3, 4, 5]
print(process_numbers(numbers, lambda x: x * 3))