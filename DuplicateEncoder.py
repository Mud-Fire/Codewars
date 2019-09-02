def duplicate_encode(word):
    # your code here
    word = word.lower()
    new_str = ''
    for i in word:
        if word.count(i) > 1:
            new_str += ")"
        else:
            new_str += "("
    return new_str


# def duplicate_encode(word):
#     # your code here
#     word = list(word.lower())
#     word1 = list(word)
#     setword = set(word)
#     for i in range(0, len(word)):
#         if word[i] in setword:
#             setword.remove(word[i])
#             word[i] = ''
#
#         elif setword == '':
#             break
#     setf = set(word)
#
#     s = ''
#     for i in range(0, len(word1)):
#         if word1[i] in setf:
#             s += ')'
#         else:
#             s += '('
#     return s
