def mix(s1, s2):
    # your code
    result = []
    for i in range(ord('a'), ord('z') + 1):
        elem = None
        s1_number = s1.count(chr(i))
        s2_number = s2.count(chr(i))
        if s1_number > 1 or s2_number > 1:
            if s1_number > s2_number:
                elem = '1:' + chr(i) * s1_number
                result.append([elem, str(len(elem)) + 'c' + chr(ord('z') - ord(elem[2]))])
            elif s1_number < s2_number:
                elem = '2:' + chr(i) * s2_number
                result.append([elem, str(len(elem)) + 'b' + chr(ord('z') - ord(elem[2]))])
            else:
                elem = '=:' + chr(i) * s1_number
                result.append([elem, str(len(elem)) + 'a' + chr(ord('z') - ord(elem[2]))])

    def takeSecond(elem):
        return elem[1]

    result.sort(key=takeSecond, reverse=True)
    return "/".join(a[0] for a in result)

print(mix("Are they here", "yes, they are here"))
