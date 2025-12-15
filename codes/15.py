class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True
        print("Inserted")

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                print("Word not found")
                return
            node = node.children[ch]
        if node.end:
            print("Word found")
        else:
            print("Word not found")

    def display(self, node, prefix):
        if node.end:
            print(prefix)
        for ch in node.children:
            self.display(node.children[ch], prefix + ch)

trie = Trie()

while True:
    print("\n1.Insert  2.Search  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        trie.insert(input("Enter word: "))
    elif ch == 2:
        trie.search(input("Enter word: "))
    elif ch == 3:
        print("Words in Trie:")
        trie.display(trie.root, "")
    elif ch == 4:
        break
    else:
        print("Invalid choice")
