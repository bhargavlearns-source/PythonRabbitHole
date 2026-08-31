#This is a good DSA level question.
#I havee pasted the code snippet from chatgpt with proper explanation, try to observe the answer if not able to crack it yourself.
#Fun fact: I was not able to solve it myself lol ;)
# Q6. Longest Substring Without Repeating Characters

s = "abcabcbb"

max_length = 0

# Start from every possible position
for i in range(len(s)):

    current = ""

    # Move forward from that position
    for j in range(i, len(s)):

        # If character is already present, stop
        if s[j] in current:
            break

        # Otherwise add it
        current += s[j]

    # Check if this substring is the longest so far
    if len(current) > max_length:
        max_length = len(current)

print(max_length)