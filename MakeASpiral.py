import numpy as np


def spiralize(size):
    spiral = np.zeros((size, size))
    if size == 1:
        return [[1]]
    if size == 2:
        return [[1, 1], [0, 1]]

    num = 0
    tag = size - 1
    for k in range(int(np.ceil(size / 2) - 1)):
        print(k)
        print(spiral)
        spiral[k, k:tag + 1] = 1 - num
        spiral[tag, k:tag + 1] = 1 - num
        spiral[k:tag + 1, k] = 1 - num
        spiral[k:tag + 1, tag] = 1 - num
        spiral[k + 1, k] = num
        tag -= 1
        num = 1 - num

    if size % 2 == 1:
        spiral[int(size / 2), int(size / 2)] = 1 - num
    elif (size/2) % 2 == 1:
        print('kkdkk')
        spiral[tag - 1, tag - 1:tag + 1] = 1 - num
        spiral[tag, tag - 1:tag + 1] = 1 - num
        spiral[tag - 1:tag + 1, tag - 1] = 1 - num
        spiral[tag - 1:tag + 1, tag] = 1 - num
        spiral[tag, tag - 1] = num

    print('######')
    print(spiral)
    return spiral.tolist()


print(spiralize(22))
