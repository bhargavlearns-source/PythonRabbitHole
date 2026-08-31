'''
A perfect number is a positive integer that equals 
the sum of its proper divisors (all divisors excluding itself).
'''
num = int(input("Enter your number:"))
factors = []
for i in range(1,num):
    if num%i == 0:
        factors.append(i)

#now if sum of factos list will be equal to the number itself, it means it worked!
if sum(factors) == num:
    print(f"{num} is a perfect number") #I have used fstring here, it means if you put f before a string in print, you can input variables into that string using {}!

else:
    print(f"{num} is not a perfect number")
