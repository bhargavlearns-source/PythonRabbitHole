a= "aaabbccccdaa"
current = "a"
count = 0
result = ""
for i in a:
    if i == current:
        count += 1
    else:
        result = result + f"{current}{count}"
        current = i
        count = 1
result = result + f"{current}{count}"
print(result)

