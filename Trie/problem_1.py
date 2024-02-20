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

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        return self._get_words(node, prefix)

    def _get_words(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for char, child_node in node.children.items():
            result.extend(self._get_words(child_node, prefix + char))
        return result

keywords = ["apple", "app", "application", "banana", "ball"]
trie = Trie()
for keyword in keywords:
    trie.insert(keyword)

prefix = "app"
autocomplete_options = trie.search(prefix)
print("Autocomplete options for prefix '{}':".format(prefix))
print(autocomplete_options)
