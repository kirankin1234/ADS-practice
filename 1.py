stack = []

def push():
    item = int(input("Enter element to push: "))
    stack.append(item)
    print("Pushed:", item)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        print("Popped:", stack.pop())

def display():
    print("Stack:", stack)

while True:
    print("\n1.Push  2.Pop  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")







queue = []

def enqueue():
    item = int(input("Enter element to insert: "))
    queue.append(item)
    print("Inserted:", item)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        print("Deleted:", queue.pop(0))

def display():
    print("Queue:", queue)

while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

ll = LinkedList()

while True:
    print("\n1.Insert  2.Display  3.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        ll.insert()
    elif ch == 2:
        ll.display()
    elif ch == 3:
        break
    else:
        print("Invalid choice")




