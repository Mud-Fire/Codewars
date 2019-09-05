import math

cache = {}
def fib_neg(n):
    a, b = 0, 1
    while n < 0:
        a, b = b - a, a
        n += 1
    return a


def fib_quick(n):
    global cache
    if n == 0:
        return 0
    elif n <= 2:
        return 1

    k = n // 2
    a = fib_quick(k)
    b = fib_quick(k + 1)

    if n % 2:
        cache[n] = a * a + b * b
    else:
        cache[n] = a * (2 * b -a)
    return cache[n]

def fib(n):
    """Calculates the nth Fibonacci number"""
    print('n: {}'.format(n))
    if n < 0:
        return fib_neg(n)
    else:
        return fib_quick(n)


