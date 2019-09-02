def queue_time(customers, n):
    # TODO
    if not customers:
        return 0
    queue = customers[0:n]
    for i in range(n, len(customers)):
        index = queue.index(min(queue))
        queue[index] += customers[i]
    return max(queue)


# Test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
# Test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
# Test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
# Test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
# Test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
# Test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")