def solution(string, markers):
    # your code here
    string = string.split("\n")
    i = 0
    while i < len(string):
        for j in range(len(string[i])):

            if string[i][j] in markers:
                string[i] = string[i][0:j]
                string[i] = string[i].rstrip()
                break
        i += 1
    return '\n'.join(string)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
