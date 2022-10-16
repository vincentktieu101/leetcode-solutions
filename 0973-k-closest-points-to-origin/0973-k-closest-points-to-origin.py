import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            distance = (x ** 2 + y ** 2) ** 1/2
            heapq.heappush(h, (distance, [x, y]))
        ans = []
        for i in range(k):
            curr = heapq.heappop(h)
            ans.append(curr[1])
        return ans