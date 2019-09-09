import numpy as np


def isValidWalk(walk):
    # determine if walk is valid
    if len(walk) != 10:
        return False
    dic = {
        's': np.array([1, 0]),
        'n': np.array([-1, 0]),
        'w': np.array([0, 1]),
        'e': np.array([0, -1])
    }
    result = np.array([0, 0])
    for i in walk:
        result += dic[i]
    if result.tolist() == [0, 0]:
        return True
    else:
        return False

print(isValidWalk(['n', 's']))
print(isValidWalk(['s', 'w', 'e', 'w', 'n', 'w', 'w', 'e', 's', 'w']))
