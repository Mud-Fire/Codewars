def memorize(func):
    cache = {}

    def warrper(*args):
        if args in cache:
            return cache[args]
        result = cache[args] = func(*args)
        return result

    return warrper


@memorize
def computer(K, maxn):
    return sum(1 / (K * pow(N + 1, 2 * K)) for N in range(1, maxn + 1))


def doubles(maxk, maxn):
    # your code
    return sum(computer(K, maxn) for K in range(1, maxk + 1))


print(doubles(20, 10000), 0.6930471955575918)
print(doubles(90, 10000))
