"""
A part:

A1. b byte code
A2. c tuple
A3. a True 
A4. b 
A5. b 
A6. {}
A7. b
A8. c
A9. b
A10. b

B part:
B1. True
B2. {‘a’:1}
B3. [1,9,25]
B4. True, False, True, False
B5. 1,2,1
B6. 0,1,2
B7. 0,1,2
B8. Error 

C part:
C1. Both the functions calls were using the same list, but the user wanted two different list, for that we locally make a list.
def add_item(item):
    my_list = []
    my_list.append(item)
    return my_list


print(add_item(1))
print(add_item(2))
C2. There was an unintentional line of code.


# C2.
# def make_multiplier(n):
def make_multiplier(n):
    def multiply(x):
        return x * n
    n = n * 10   # <-- something's off here
    return multiply


times5 = make_multiplier(5)
print(times5(2))



C3. The for loop didnt work because we break the program so the loop terminated after the total is > 5, which it will be. There for either we can just remove the loop or we can simply continue the iterations and put total underneath it.
total = 0
for i in range(5):
    if total > 5:
        continue
    total = total + i
else:
    print("Loop finished without breaking")
print(total)

C4. If the key is not available in the dict, it will raise a value.
def get_value(d, key):
    if key in d:
        value = d[key]
        return value
    else:
        return None


print(get_value({'a': 1}, 'b'))
C5.
Even though the oops was not part of this test here is the solution and fixed code snippet:
class Counter:
    count = 0
    def increment(cls):
        cls.count = cls.count + 1
        return cls.count


c = Counter()
print(c.increment())

D Part:
D1.
sq = [x**3 for x in range(1,21) if x%3==0]
print(sq)
D2.
def make_power(n):
    def exp(y):
        return y**n
    return exp


square = make_power(2)
s = square(10)
print(s)

D3.

def running_total():
    sum = 0
    count = 0
    def add():
        nonlocal sum
        nonlocal count
        count = count + 1
        sum += count
        return sum
    return add


x = running_total()
print(x())
print(x())
print(x())

D4.


data = [('a', 3), ('b', 1), ('c', 2)]
result = sorted(data, key = lambda x: x[1], reverse = True)
print(result)

D5.
def countdown(n):
    for i in range(n, 0, -1):
        yield i


c1 = countdown(5)
for i in c1:
    print(i)

D6.
nums = [1, 2, 3, 4, 5, 6, 7, 8]


even_num = list(filter(lambda x: x%2 ==0, nums))
even_num_cub = list(map(lambda x: x**3, even_num))
print(even_num_cub)

D7.
def make_accumulator():
    total = 0
    def add(x):
        nonlocal total
        total = total + x
        return total
    return add


acc = make_accumulator()
print(acc(10))


print(acc(5))


"""