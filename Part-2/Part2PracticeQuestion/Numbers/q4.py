import math
reverse = 0
num = int(input("Enter your number:"))
is_prime = True


for i in range(2,num):
    if num % i ==0:
        print(f"{num} is a composite!")
        is_prime = False
        break

if num>=2:
    if is_prime:
        print(f"{num} is a prime!")
else:
    print(f"{num} is Neither prime not composite!")



result = math.isqrt(num)

if result * result == num:
    print(f"{num} is a Perfect square")

else:
    print(f"{num} is not a Perfect square")

tempnum = num

while tempnum !=0:
    digit = tempnum %10 
    reverse = reverse * 10 + digit 
    tempnum = tempnum // 10 

if reverse == num: 
    print(f"{num} is a palindrome")

else:
    print(f"{num} is not a palindrome")


