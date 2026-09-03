def average(*args):
    sum = 0
    for i in args:
        sum += i
    if len(args) != 0:
        return sum/(len(args))
    else:
        return ("Enter some numbers!")

print(average())