def max_multiple(divisor, bound):
    # your code here
    return bound - bound % divisor


print(max_multiple(7, 100), 98)
