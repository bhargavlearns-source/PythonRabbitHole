marks = 72

if marks>100:
    print("Invalid marks") #Take the edge cases first

elif marks>=90 and marks<101:
    print("A")

elif marks>=75 and marks<90:
    print("B")

elif marks>=60 and marks<75:
    print("C")

elif marks>=40 and marks<60:
    print("B")

elif marks<40:
    print("Fail")

else:
    print("Invalid marks!")