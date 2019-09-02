# def get_pins(observed):
#     '''TODO: This is your job, detective!'''
#     dic = {
#         '1': ['1', '2', '4'],
#         '2': ['1', '2', '3', '5'],
#         '3': ['2', '3', '6'],
#         '4': ['1', '4', '5', '7'],
#         '5': ['2', '4', '5', '6', '8'],
#         '6': ['3', '5', '6', '9'],
#         '7': ['4', '7', '8'],
#         '8': ['0', '5', '7', '8', '9'],
#         '9': ['6', '8', '9'],
#         '0': ['0', '8']
#     }
#     result = []
#     data = []
#     k = len(observed)
#     num = 1
#     for i in observed:
#         data.append(dic[i])
#     result = data[0]
#     for i in range(len(data)):
#         curr = result
#         result = []
#         for j in curr:
#             if i < (len(data) - 1):
#                 for k in data[i + 1]:
#                     result.append(j + k)
#             else:
#                 result = curr
#     return result
def get_pins(observed):
    '''TODO: This is your job, detective!'''
    dic = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }
    if len(observed) == 1:
        return dic[observed]
    else:
        return [a + b for a in dic[observed[0]] for b in get_pins(observed[1:])]


tup = ('8457', ['5', '7', '8', '9', '0'])
print(get_pins(tup[0]))
