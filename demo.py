'''
Trie Data Structure

A Trie is a special type of tree used to efficiently store a set of strings. It is a type of prefix tree that helps in storing words in a way that 
allows for fast retrieval based on their prefixes. It is particularly useful for:
- **Prefix search**: Finding all words that begin with a specific prefix.
- **Autocompletion**: Suggesting words based on a given prefix.
- **Dictionary-like operations**: Efficiently checking whether a word exists in a set of words.

### How does a Trie work?
1. **Structure**: A Trie consists of nodes where each node represents a character. The root node is empty (it doesn't represent any character).
   
2. **Inserting a Word**: 
   - To insert a word, start at the root node and for each character in the word:
     - If the character does not exist as a child of the current node, create a new node for that character.
     - Move to the child node corresponding to that character.
   - Once all characters of the word are processed, mark the last node as the "end of the word."

3. **Searching for a Word**: 
   - To search for a word, start from the root node and follow the path corresponding to each character in the word.
   - If any character is not found in the current node's children, the word does not exist in the Trie.
   - If all characters are found and the last node is marked as "end of the word," the word exists in the Trie.

4. **Efficiency**: 
   - **Time Complexity for Insertion and Search**: O(k), where 'k' is the length of the word being inserted or searched.
   - **Space Complexity**: O(n * k), where 'n' is the number of words and 'k' is the average length of a word. Each word takes space proportional to its length.

### Advantages of a Trie:
- **Fast Prefix Search**: Since nodes with the same prefix are shared, it becomes easy to find all words with a common prefix.
- **Efficient Word Search**: Searching for a word can be done in O(k) time where k is the length of the word.

'''

class TrieNode():
    def __init__(self):
        '''
        Each TrieNode contains:
        - children: a dictionary mapping characters to child TrieNodes
        - end_of_the_word: a boolean indicating if this node completes a word
        '''
        self.children = {}
        self.end_of_the_word = False
    

class Trie():
    def __init__(self):
        '''
        Initializes the Trie with an empty root TrieNode
        '''
        self.root = TrieNode()

    def insert(self, word):
        '''
        Inserts a word into the Trie.
        For each character in the word:
        - If it doesn't exist in the current node's children, create a new TrieNode
        - Move to the child node
        Finally, mark the last node's end_of_the_word as True
        '''
        node = self.root
        for _char in word:
            if _char not in node.children:
                node.children[_char] = TrieNode()
            node = node.children[_char]
        node.end_of_the_word = True

    def search(self, word):
        '''
        Searches for a word in the Trie.
        For each character in the word:
        - If it doesn't exist in the current node's children, return False
        - Move to the next node
        Finally, return True only if the last node marks the end of a word
        '''
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_the_word


def main():
    trie = Trie()
    trie.insert("cat")
    print(trie.search("cat"))  # Output: True

    '''
    After inserting "cat", the Trie structure looks like:

    root.children = {
        'c': TrieNode(children={
            'a': TrieNode(children={
                't': TrieNode(
                    children={},
                    end_of_the_word=True
                )
            }, 
            end_of_the_word=False)
        }, 
        end_of_the_word=False)
    }
    '''

if __name__ == "__main__":
    main()
