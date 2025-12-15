class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        balance = self.balance(root)

        # Left Left
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)

        # Right Right
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)

        # Left Right
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

avl = AVLTree()
root = None

while True:
    print("\n1.Insert  2.Display(Inorder)  3.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        root = avl.insert(root, int(input("Enter element: ")))
    elif ch == 2:
        print("AVL Tree (Inorder):", end=" ")
        avl.inorder(root)
        print()
    elif ch == 3:
        break
    else:
        print("Invalid choice")
