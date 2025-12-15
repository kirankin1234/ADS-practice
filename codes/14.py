class KDNode:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

def insert(root, point, depth=0):
    if root is None:
        return KDNode(point)

    cd = depth % 2  # 0 for x, 1 for y

    if point[cd] < root.point[cd]:
        root.left = insert(root.left, point, depth+1)
    else:
        root.right = insert(root.right, point, depth+1)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.point, end=" ")
        inorder(root.right)

root = None
n = int(input("Enter number of points: "))

for _ in range(n):
    x, y = map(int, input("Enter x y: ").split())
    root = insert(root, (x, y))

print("KD Tree Inorder:")
inorder(root)





class QuadNode:
    def __init__(self, x, y):
        self.point = (x, y)
        self.NW = None
        self.NE = None
        self.SW = None
        self.SE = None

def insert(root, x, y):
    if root is None:
        return QuadNode(x, y)

    rx, ry = root.point

    if x < rx and y >= ry:
        root.NW = insert(root.NW, x, y)
    elif x >= rx and y >= ry:
        root.NE = insert(root.NE, x, y)
    elif x < rx and y < ry:
        root.SW = insert(root.SW, x, y)
    else:
        root.SE = insert(root.SE, x, y)

    return root

def display(root):
    if root:
        print(root.point, end=" ")
        display(root.NW)
        display(root.NE)
        display(root.SW)
        display(root.SE)

root = None
n = int(input("Enter number of points: "))

for _ in range(n):
    x, y = map(int, input("Enter x y: ").split())
    root = insert(root, x, y)

print("Quad Tree Points:")
display(root)







class PSTNode:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

def insert(root, point):
    if root is None:
        return PSTNode(point)

    # Heap property on y
    if point[1] > root.point[1]:
        root.point, point = point, root.point

    # BST property on x
    if point[0] < root.point[0]:
        root.left = insert(root.left, point)
    else:
        root.right = insert(root.right, point)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.point, end=" ")
        inorder(root.right)

root = None
n = int(input("Enter number of points: "))

for _ in range(n):
    x, y = map(int, input("Enter x y: ").split())
    root = insert(root, (x, y))

print("Priority Search Tree:")
inorder(root)
