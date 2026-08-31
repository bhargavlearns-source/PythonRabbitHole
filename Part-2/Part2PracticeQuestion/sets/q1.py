A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

setA = set(A)
setB = set(B)
print(f"Common elements:{setA.intersection(setB)}")

print(f"Common elements:{setA.difference(setB)}")

print(f"Common elements:{setB.difference(setA)}")

print(f"Common elements:{setA.union(setB)}")