def pig_it(text):
    text_list = text.split(" ")
    for i in range(0,len(text_list)):
        if text_list[i].isalpha():
            text_list[i] = text_list[i] + text_list[i]
            text_list[i] = text_list[i][1:int(len(text_list[i])/2+1)] + "ay"
    return " ".join(text_list)


print(pig_it('This is my string'))

