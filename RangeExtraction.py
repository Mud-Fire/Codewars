def solution(args):
    # your code here
    result = []
    i = 0
    while i < len(args):
        j = i
        while j + 1 < len(args) and args[j+1] - args[j] == 1:
            j += 1
        if j != i and j - i > 1:
            result.append('%d-%d'%(args[i], args[j]))
            i = j+1
        else :
            result.append(str(args[i]))
            i += 1

    return ','.join(result)

    pass


# print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]),
#       '-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]), '-3--1,2,10,15,16,18-20')
