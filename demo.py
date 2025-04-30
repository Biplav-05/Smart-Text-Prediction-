# First need to define the node structure because value and its status for next childern will be stored in node.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_the_word = False
    

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for _char in word:
            if _char not in node.children:
                node.children[_char]= TrieNode()
            node = node.children[_char]
        node.end_of_the_word=True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_the_word

# The main function to run tests
def main():
    trie = Trie()  # Create a new Trie instance

    # Insert words into the trie
    trie.insert("cat")
    print(trie.search("cat"))


# Run the main function
if __name__ == "__main__":
    main()