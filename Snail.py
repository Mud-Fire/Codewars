import numpy as np


def snail(snail_map):
    snail_map = np.array(snail_map)
    result = list(snail_map[0])

    while snail_map.any():
        snail_map = np.delete(snail_map,0, axis=0)
        if snail_map is not None:
            snail_map = np.rot90(snail_map, 1)
        result += list(snail_map[0])
    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(snail(array))
