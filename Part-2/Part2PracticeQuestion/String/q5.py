
s= "A man, a plan, a canal: Panama"
reverse = ""
result = ""
for i in s:
    if i.lower() not in (",",":", " " ):
        result = result + i.lower()

for i in s:
    if i.lower() not in (",",":", " " ):
        reverse =  i.lower() + reverse

# print(result)
# print(reverse)
if result == reverse:
    print(f"{s} is a palindrome string!")