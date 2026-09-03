def create_multiplier(n):
    def multiplier(num):
        return n * num
    return multiplier

double = create_multiplier(2)
print(double(10))