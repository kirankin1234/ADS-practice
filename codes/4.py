class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.skip = None   # level 1 pointer

class SkipList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        count = 0
        prev = None

        while temp:
            prev = temp
            temp = temp.next
            count += 1

        prev.next = new

        # fixed skip logic (every 2nd node)
        if count % 2 == 0:
            prev.skip = new

    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                print("Found")
                return
            if temp.skip and temp.skip.data <= key:
                temp = temp.skip
            else:
                temp = temp.next
        print("Not Found")

    def display(self):
        print("Level 0:")
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("NULL")

        print("Level 1:")
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.skip
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
