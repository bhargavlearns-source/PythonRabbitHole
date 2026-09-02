numbers = [10,25,30,45,50]
target = 30
isfound = False
for i in numbers:
    if i == target:
        isfound = True

if isfound:
    print("found!")
else:
    print("Not found!")
