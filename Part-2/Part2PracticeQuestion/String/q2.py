s = "aabbcddeff"
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else: 
        dic[i] = 1

for i in dic.keys():
    if dic[i] ==1:
        print(i)
        break
