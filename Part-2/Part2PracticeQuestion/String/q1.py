s = "programming"
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)