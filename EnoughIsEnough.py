# Delete occurrences of an element if it occurs more than n times
def delete_nth(order, max_e):
    or_list = list(set(order))
    order.reverse()
    for i in or_list:
        k = order.count(i)
        while k - max_e > 0:
            order.remove(i)
            k -= 1
    order.reverse()
    return order
    # code here

# Test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
# Test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
