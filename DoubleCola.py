import math


def who_is_next(names, r):
    # your code
    length = len(names)

    k = int(math.log(r / length + 1, 2))
    num = r - length * (2 ** k - 1)
    index = math.ceil(num / (2 ** k))
    return names[index - 1]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(who_is_next(names, 2))
