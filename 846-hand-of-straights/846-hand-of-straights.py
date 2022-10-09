class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        d = {
            1: 1,
            2: 2,
            3, 2,
            4: 1,
            6: 1,
            7: 1,
            8: 1
        }
        
        
        """
        
        if len(hand) % groupSize != 0: return False
        
        d = defaultdict(int)
        
        for card in hand:
            d[card] += 1
        
        while d:
            lowest = min(d.keys())
            for card in range(lowest, lowest + groupSize):
                d[card] -= 1
                if d[card] == -1:
                    return False
                if d[card] == 0:
                    del d[card]
        
        return True