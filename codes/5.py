class Node:
    def __init__(self, data, level):
        self.data = data
        self.forward = [None]*(level+1)

class SkipList:
    def __init__(self):
        self.head = Node(-1, 2)
        self.count = 0

    def insert(self, data):
        self.count += 1

        if self.count % 2 == 0:
            level = 1
        else:
            level = 0

        new = Node(data, level)
        curr = self.head

        for i in range(level, -1, -1):
            while curr.forward[i]:
                curr = curr.forward[i]
            curr.forward[i] = new

    def search(self, key):
        curr = self.head
        for i in range(1, -1, -1):
            while curr.forward[i] and curr.forward[i].data < key:
                curr = curr.forward[i]
        curr = curr.forward[0]
        print("Found" if curr and curr.data == key else "Not Found")

    def display(self):
        for i in range(1, -1, -1):
            curr = self.head.forward[i]
            print("Level", i, ":", end=" ")
            while curr:
                print(curr.data, end=" -> ")
                curr = curr.forward[i]
            print("NULL")

sl = SkipList()

while True:
    print("\n1.Insert 2.Search 3.Display 4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        sl.insert(int(input("Enter element: ")))
    elif ch == 2:
        sl.search(int(input("Enter element: ")))
    elif ch == 3:
        sl.display()
    else:
        break
