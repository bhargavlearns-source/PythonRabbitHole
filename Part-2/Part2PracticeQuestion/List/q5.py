L = [4, 3, 2, 7, 8, 2, 3, 1]
seen = []
dublicate = []
for i in L:
    if i in seen:
        dublicate.append(i)
    else:
        seen.append(i)
print(dublicate)