def productFib(prod):
    x1 = 0
    x2 = 1
    while x1 * x2 < prod:
        x1, x2 = x2, x1 + x2
    return [x1, x2, x1 * x2 == prod]


print(productFib(4895))
print(productFib(5895))
