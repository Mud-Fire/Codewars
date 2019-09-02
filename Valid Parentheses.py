def valid_parentheses(string):
    list_str = list(string)
    #your code here

    sub_list = list()
    for i in list_str:
        if i == "(":
            sub_list.append('(')
        elif i == ")":
            if not sub_list:
                return False
            else:
                sub_list.pop()
    if not sub_list:
        return True
    else:
        return False