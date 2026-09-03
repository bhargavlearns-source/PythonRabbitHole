def power(number, power=2):
    result = 1
    for i in range(power):
        result = result * number
    return result

print(power(5))