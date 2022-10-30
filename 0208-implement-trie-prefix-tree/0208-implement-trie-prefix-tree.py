class Trie:
    # last solved: 10/2022, difficulty: 3/5
    
    def __init__(self):
        self.values = {}
        self.end = False

    def insert(self, word: str) -> None:
        if word == "":
            self.end = True
            return
        value, rest = word[0], word[1:]
        trie = self.values.get(value, Trie())
        trie.insert(rest)
        self.values[value] = trie

    def search(self, word: str) -> bool:
        if word == "": return self.end
        value, rest = word[0], word[1:]
        if value not in self.values: return False
        return self.values[value].search(rest)

    def startsWith(self, prefix: str) -> bool:
        word = prefix
        if word == "": return True
        value, rest = word[0], word[1:]
        if value not in self.values: return False
        return self.values[value].startsWith(rest)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)