d = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 2
}
dic = {}
for i, j in d.items():
    if j not in dic:
        dic[j] = []
    dic[j].append(i)

print(dic)