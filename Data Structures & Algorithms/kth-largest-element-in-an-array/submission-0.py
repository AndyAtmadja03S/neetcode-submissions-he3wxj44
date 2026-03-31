class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        negate_num = [-n for n in nums]
        for num in negate_num:
            heapq.heappush(heap, num)
        
        for _ in range(1,k):
            heapq.heappop(heap)

        return heap[0] * -1