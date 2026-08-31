n = 583927
templist = []
reverse = 0
while n!=0:
    digit = n%10 #7 #2 #9 #3 #8 #5
    reverse = reverse * 10 + digit
    templist.append(digit)
    n = n//10 #58392 #5839 #583 #58 #5 

print("Largest digit:", max(templist))
print("Smallest digit:", min(templist))
print("Sum of all digits:", sum(templist))
print("Reverse:", reverse)
    