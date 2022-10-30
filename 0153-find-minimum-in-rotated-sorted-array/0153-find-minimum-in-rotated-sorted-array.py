class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            print(start, end)
            m = start + (end - start) // 2
            if nums[m] > nums[end]:
                start = m + 1
            else:
                end = m
        return nums[start]