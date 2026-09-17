import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(-count, key) for key, count in counts.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            neg_count, key = heapq.heappop(heap)
            result.append(key)
        return result