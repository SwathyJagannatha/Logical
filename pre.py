class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root is None:
        return

    # Visit the root node
    print(root.data, end=" ")

    # Traverse the left subtree
    pre_order_traversal(root.left)

    # Traverse the right subtree
    pre_order_traversal(root.right)

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

    print("Pre-Order Traversal: ", end="")
    pre_order_traversal(root)
    print()