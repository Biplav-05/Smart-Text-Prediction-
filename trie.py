# Found the inbuilt Ubuntu dictionary inside '/usr/share/dict/words',
# so using it to feed data to trie, and when user searches, we use prefix search

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_the_word=False

class Trie():
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word : str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node = node.children[char]
        node.end_of_the_word=True
        # print(f'inserted word = {word}')

    def prefix_search(self, prefix_word:str):
        node =self.root
        result = []
        for char in prefix_word:
            if char in node.children:
                node = node.children[char]
            else:
                return result


        # Step 2: Perform DFS to find all words with the given prefix
        def dfs(current_node, current_word):
            if current_node.end_of_the_word:
                result.append(current_word)

            for char, child_node in current_node.children.items(): # he => hello
                dfs(child_node, current_word + char)

        # Step 3: Start DFS from the node found
        dfs(node, prefix_word)
        return result


def main():
    obj = Trie()
    with open('/usr/share/dict/words', 'r') as file:
        for line in file:
            word = line.strip().lower()
            if word.isalpha:
                obj.insert(word)
    p_s = obj.prefix_search('hel')
    print(p_s)
if __name__ == "__main__":
    main()
