class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        
        for i, letter in enumerate(s):
            if d[letter] == 1:
                return i
        
        return -1