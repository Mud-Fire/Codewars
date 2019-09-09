import numpy as np


def mystery(n):
    if n == 0:
        return 0
    address = int(np.log2(n))
    result = 0
    while n > 1:
        n = 2 ** address - (n - 2 ** address) - 1
        result += 2 ** address
        if n == 0:
            return result + 0
        address = int(np.log2(n))
    if n == 0:
        return result + 0
    else:
        return result + 1
    pass


def mystery_inv(n):
    str_bn = bin(n).split('b')[1]
    result = 0
    if len(str_bn) == 1:
        if str_bn[0] == '1':
            result = 1
        if str_bn[0] == '0':
            result = 0
    else:
        k = str_bn[0]
        if k == '1':
            str_bn = str_bn[1:]
            result += 2 ** (len(str_bn)+1) - mystery_inv(int(str_bn, 2)) - 1
    return result


def name_of_mystery():
    return "Gray code"
    pass

print(mystery(9), 13, "mystery_inv(5)")
# # test.assert_equals(mystery(9), 13, "mystery(9) ")
# print(mystery_inv(13), 9, "mystery_inv(13)")
print(mystery(19), 26, "mystery(19) ")
# test.assert_equals(mystery_inv(26), 19, "mystery_inv(26)")
