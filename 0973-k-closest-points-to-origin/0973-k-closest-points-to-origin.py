import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # last solved: 10/2022, difficulty: 3/5
        h = []
        for x, y in points:
            distance = (x ** 2 + y ** 2) ** 1/2
            h.append((distance, [x, y]))
        heapq.heapify(h)
        ans = []
        for i in range(k):
            curr = heapq.heappop(h)
            ans.append(curr[1])
        return ans