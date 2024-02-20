class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word

dictionary = ["apple", "banana", "cherry", "orange"]
trie = Trie()
for word in dictionary:
    trie.insert(word)

word_to_check = "banana"
if trie.search(word_to_check):
    print("{} is spelled correctly.".format(word_to_check))
else:
    print("{} is misspelled.".format(word_to_check))
