def numbersone(num):
    str_num = str(bin(num)).split('b')[1]
    result = 0
    for i in range(len(str_num)):
        n, m = divmod(num, 2 ** (i + 1))
        result += n * (2 ** i)
        if m > (2 ** i - 1):
            result += (m - 2 ** i + 1)
    return result


def countOnes(left, right):
    left_one = numbersone(left)
    right_one = numbersone(right)
    return right_one - left_one + str(bin(left)).split('b')[1].count('1')


print(countOnes(12, 29))
