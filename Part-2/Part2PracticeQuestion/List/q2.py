#This is my fav question from the practice question list!
L = [10, 45, 20, 45, 30]
firstlargest = 0
SecondLargest = 0

for i in L:
    if firstlargest < i:
        firstlargest = i

    elif firstlargest > i and i > SecondLargest:
        SecondLargest = i

print(firstlargest)
print(SecondLargest)


