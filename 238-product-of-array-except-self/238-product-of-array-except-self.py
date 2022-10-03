class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1 for num in nums]
        left = [1 for num in nums]
        
        n = len(nums)
        
        curr = 1
        for i in range(n):
            right[i] = curr
            curr *= nums[i]
        
        curr = 1
        for i in range(n - 1, -1, -1):
            left[i] = curr
            curr *= nums[i]

        ans = []
        for i in range(n):
            ans.append(right[i] * left[i])
        return ans
    
    
    
    