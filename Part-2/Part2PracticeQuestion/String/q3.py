sentence = "Python makes programming surprisingly enjoyable"
dic= {}
maximun = 0
emptystring = 0
for i in sentence.split(" "):
    if len(i) > maximun:
        maximun = len(i)
        emptystring = i

print(emptystring)