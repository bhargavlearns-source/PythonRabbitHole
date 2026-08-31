d1 = {
    "a": 10,
    "b": 20
}

d2 = {
    "b": 5,
    "c": 30
}

l = [d1,d2]
dic = {}

for i in l:
    for j,m in i.items():
        if j not in dic:
            dic[j] = m
        else:
            dic[j] += m



print(dic)