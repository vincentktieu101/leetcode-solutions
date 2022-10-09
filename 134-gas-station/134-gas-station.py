class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        [1,2,3,4,5]
        [3,4,5,1,2]
        
        [-2,-2,-2,3,3]
        """
        
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        
        if sum(diff) < 0: return -1
        
        ans = 0
        extra = 0
        
        for i in range(len(diff)):
            extra += diff[i]
            
            if extra < 0:
                ans = i + 1
                extra = 0
        
        return ans
                