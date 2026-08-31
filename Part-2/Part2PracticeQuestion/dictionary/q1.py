text = "python is easy and python is powerful"
dic = {}
for i in text.split(" "):
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
    