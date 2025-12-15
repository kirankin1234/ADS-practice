class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            new_node.color = "BLACK"
            self.root = new_node
            return

        temp = self.root
        parent = None

        while temp:
            parent = temp
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        new_node.parent = parent
        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u and u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u and u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)

        self.root.color = "BLACK"

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, root.color, end="  ")
            self.inorder(root.right)

rbt = RedBlackTree()

while True:
    print("\n1.Insert  2.Display(Inorder)  3.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        rbt.insert(int(input("Enter element: ")))
    elif ch == 2:
        print("Red Black Tree:")
        rbt.inorder(rbt.root)
        print()
    else:
        break
