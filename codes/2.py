size = 10
hash_table = [None] * size

def hash_function(key):
    return key % size

def insert():
    key = int(input("Enter key: "))
    index = hash_function(key)

    while hash_table[index] is not None:
        index = (index + 1) % size

    hash_table[index] = key
    print("Key inserted")

def search():
    key = int(input("Enter key to search: "))
    index = hash_function(key)

    while hash_table[index] is not None:
        if hash_table[index] == key:
            print("Key found at index", index)
            return
        index = (index + 1) % size

    print("Key not found")

def display():
    print("Hash Table:")
    for i in range(size):
        print(i, ":", hash_table[i])

while True:
    print("\n1.Insert  2.Search  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        insert()
    elif ch == 2:
        search()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
