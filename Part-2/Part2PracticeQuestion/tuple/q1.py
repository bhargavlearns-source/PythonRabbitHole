a = 10
b = 20

(a,b) = (b,a)
print(a,b)
print("""
What happens during tuple unpacking swap:
1. Python evaluates the RIGHT side first: (b, a) creates a tuple (20, 10)
2. This tuple exists temporarily in memory
3. Then Python unpacks it to the LEFT side: a, b
4. a gets the first value (20), b gets the second value (10)

This is atomic - no temp variable needed because Python evaluates
the entire right side before any assignment happens.
""") 