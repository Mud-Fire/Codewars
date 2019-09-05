# Task
# You are given a string s. Every letter in s appears once.
#
# Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)
#
# Example
# For s = "abc", the result should be "bac". The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".
#
# Input/Output
# [input] string s
#
# unique letters (2 <= length <= 26)
#
# [output] a string
#
# middle permutation.

def middle_permutation(string):
    # your code here
    string_list = sorted(string)
    string = ''.join(string_list)
    if len(string) % 2 == 0:
        k = int(len(string)/2)-1
        string = string[0:k] +string[k+1:] + string[k]
        return string[::-1]
    else:
        k = int(len(string) / 2)
        return string[k] + middle_permutation(string[0:k] + string[k+1:])


print(middle_permutation("abxcd"))
