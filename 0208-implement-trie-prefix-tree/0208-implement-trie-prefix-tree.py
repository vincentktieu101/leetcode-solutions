class Trie:
    def __init__(self):
        self.values = {}
        self.end = False

    def insert(self, word: str) -> None:
        if not word: 
            self.end = True
            return
        letter = word[0]
        if not self.values.get(letter, False):
            self.values[letter] = Trie()
        self.values[letter].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word: return self.end
        letter = word[0]
        if letter in self.values: return self.values[letter].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return True
        letter = prefix[0]
        if letter in self.values: return self.values[letter].startsWith(prefix[1:])
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)