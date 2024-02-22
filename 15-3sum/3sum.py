class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while i < j < k:
                target = -nums[i]
                if target == nums[j] + nums[k]:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                    while k > i and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif target < nums[j] + nums[k]:
                    while k > i and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                else:
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ans
