class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            
        num_count_tuple = []
        for key, value in counts.items():
            num_count_tuple.append((value, key))
            
        num_count_tuple.sort()
        
        ans = []
        for value, key in num_count_tuple[-k:]:
            ans.append(key)
        return ans