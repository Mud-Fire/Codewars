def find_uniq(arr):
    arr.sort()
    return arr[0] if arr[0] != arr[1] else arr[-1]
    # your code here
    # n: unique integer in the array
