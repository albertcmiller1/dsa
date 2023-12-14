'''
          'a'
          / 
        'l'
        /  \
    'b'    'l'    
'''

class TrieNode: 
    def __init__(self):
        self.children = {}
        self.endOfWord = False 


class Trie: 
    def __init__(self): 
        self.root = TrieNode()
    
    def insert(self, word: str) -> None: 
        curr = self.root

        for c in word: 
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        # cur is now at end 
        curr.endOfWord = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word: 
            if c not in curr.children: 
                return False 
            curr = curr.children[c]
        return curr.endOfWord
    
    def starts_with(self, prefix: str) -> bool: 
        curr = self.root
        for c in prefix: 
            if c not in curr.children: 
                return False 
            curr = curr.children[c]
        return True

trie = Trie()
trie.insert("albert")
print(trie.search("albert"))
print(trie.starts_with("albe"))

    