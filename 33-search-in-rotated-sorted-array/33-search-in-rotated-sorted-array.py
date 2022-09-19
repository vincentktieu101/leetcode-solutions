class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [4,5,6,7,0,1,2]
        
        [1,2,3,4]
        """
        # 
        l = 0
        r = len(nums) - 1
        
        while l < r: # come back to this
            m = l + (r - l) // 2
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m
                
        # assume we know where the start is
        start = l
        if nums[-1] < target:
            l = 0
            r = start - 1
        else:
            l = start
            r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1