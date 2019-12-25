def clean_string(s):
    # your code here
    result = []
    for i in s:
        if i != "#":
            result.append(i)
        elif i == "#" and result:
            result.pop()

    return "".join(result)


# print(clean_string('abc#d##c'), "ac")
# print(clean_string('abc####d##c#'), "")
# print(clean_string("#######"), "")
# print(clean_string(""), "")
