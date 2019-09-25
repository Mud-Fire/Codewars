def string_func(s, x):
    # your code
    if x == 0:
        return s
    print(x)
    do_x = x % life(len(s))
    print(do_x)
    while do_x > 0:
        for i in range(len(s)):
            s = s[:i] + s[i:][::-1]
        do_x -= 1
    return s


def life(n):
    if n <= 1:
        return 1
    m = 1
    while True:
        a = (2 ** m) % (2 * n + 1)
        if a == 1 or a == 2 * n:
            return m
        m = m + 1
#
# print(string_func("This is a string exemplification!",0),"This is a string exemplification!")
# print(string_func("String for test: incommensurability", 1), "ySttirliinbga rfuosrn etmemsotc:n i")
print(string_func("Ohh Man God Damn",7)," nGOnmohaadhMD  ")
# print(string_func("String", 6), "nrtgSi")
