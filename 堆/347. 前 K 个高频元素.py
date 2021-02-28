"""
    https://leetcode-cn.com/problems/top-k-frequent-elements/
    
    https://leetcode-cn.com/problems/top-k-frequent-elements/solution/leetcode-di-347-hao-wen-ti-qian-k-ge-gao-pin-yuan-/
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from  collections import Counter
        import heapq

        nums_counter = Counter(nums)
        heap = []
        heapq.heapify(heap)
        res = []
        for num in nums_counter:
            heapq.heappush(heap, (-nums_counter[num], num))
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res