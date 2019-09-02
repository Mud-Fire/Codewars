def in_array(array1, array2):
    # your code
    result = list()
    for i in array1:
        for j in array2:
            if i in j:
                result.append(i)
                break
    result = list(set(result))
    result.sort()
    return result


a1 = ["arp", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'strong']
print(list(set(a1)))
print(in_array(a1, a2))
