class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # last solved: 10/2022, difficulty: 2/5
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            
#         num_count_tuple = []
#         for key, value in counts.items():
#             num_count_tuple.append((value, key))
            
#         num_count_tuple.sort()
        
#         ans = []
#         for value, key in num_count_tuple[-k:]:
#             ans.append(key)
#         return ans
        
        h = []
        for key, value in counts.items():
            h.append((-value, key))
        
        heapq.heapify(h)
        
        ans = []
        for i in range(k):
            _, key = heapq.heappop(h)
            ans.append(key)
            
        return ans