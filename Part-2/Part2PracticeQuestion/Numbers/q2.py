'''An Armstrong number (also known as a narcissistic number) is a positive integer that equals the sum of its own digits, 
each raised to the power of the total number of digits in the number.
example: 153'''

num = int(input("Enter your number:"))
summ = 0
x = len(str(num))
for i in str(num):
    summ = summ + (int(i) **x )

if summ == num:
    print("The number is armstrong number!")
else:
    print("The number is not armstrong number")
