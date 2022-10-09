class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        [1,2,3,4,5]
        [3,4,5,1,2]
        
        [-2,-2,-2,3,3]
        """
        
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        extra = 0
        
        for i in range(len(gas)):
            extra += gas[i] - cost[i]
            if extra < 0:
                start = i + 1
                extra = 0
        
        return start