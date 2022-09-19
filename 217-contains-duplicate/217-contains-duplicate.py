class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # last solved: 9/2022, difficulty: 1/5
        
        d = set()
        for num in nums:
            if num in d: return True
            d.add(num)
        return False
        