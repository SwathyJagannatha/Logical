from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return

    q = deque([root])

    while q:
        current = q.popleft()

        # Visit the root node
        print(current.data, end=" ")

        # Enqueue left child
        if current.left:
            q.append(current.left)

        # Enqueue right child
        if current.right:
            q.append(current.right)

if __name__ == "__main__":
    # Create the following binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level-Order Traversal: ", end="")
    level_order_traversal(root)
    print()