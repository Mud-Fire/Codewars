class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if node is None:
        return []
    result = []
    queue = [node]

    while len(queue):
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
