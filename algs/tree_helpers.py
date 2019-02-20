class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree_from_list(arr):
    if not arr:
        return None

    len_arr = len(arr)
    head = TreeNode(arr[0])
    queue = [head]
    i = 0

    while queue:
        curr = queue.pop(0)
        if curr:
            curr.left = TreeNode(arr[2 * i + 1]) if 2 * i + 1 < len_arr else None
            curr.right = TreeNode(arr[2 * i + 2]) if 2 * i + 2 < len_arr else None
            queue.append(curr.left)
            queue.append(curr.right)
            i += 1

    return head


def bfs(node):
    q = [node]
    result = []
    while q:
        curr = q.pop(0)
        if curr:
            result.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        else:
            result.append(None)
    return result


def rec_bfs(node):
    if not node:
        return []
    return rec_bfs(node.right) + rec_bfs(node.left) + [node.val]


if __name__ == "__main__":
    test1 = [0, 1, 2, 3, 4]
    test2 = [0, None, 1, 2, 3, None, 4, None, 5]
    """
        test1:
                0 
             1     2
            3  4

        test2:
                0
                    1
                 2     3
                  4      5
    """
    print(bfs(create_tree_from_list(test1)))
    print(bfs(create_tree_from_list(test2)))
    print(rec_bfs(create_tree_from_list(test1))[::-1])
    print(rec_bfs(create_tree_from_list(test2))[::-1])
