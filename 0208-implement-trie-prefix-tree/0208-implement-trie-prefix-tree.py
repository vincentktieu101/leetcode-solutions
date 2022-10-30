class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        n = self
        for letter in word:
            if letter not in n.children:
                n.children[letter] = Trie()
            n = n.children[letter]
        n.end = True

    def search(self, word: str) -> bool:
        n = self
        for letter in word:
            if letter not in n.children: return False
            n = n.children[letter]
        return n.end

    def startsWith(self, word: str) -> bool:
        n = self
        for letter in word:
            if letter not in n.children: return False
            n = n.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)