L = [0, 1, 0, 3, 12]
result = []
for i in L:
    if i != 0:
        result.append(i)
for i in L:
    if i == 0:
        result.append(0)
print(result)