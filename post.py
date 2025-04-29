class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def post_order_traversal(root):
    if root is None:
        return

    # Traverse the left subtree
    post_order_traversal(root.left)

    # Traverse the right subtree
    post_order_traversal(root.right)

    # Visit the root node
    print(root.data, end=" ")

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

    print("Post-Order Traversal: ", end="")
    post_order_traversal(root)
    print()