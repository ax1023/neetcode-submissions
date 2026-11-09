class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-num for num in nums]

        k_th = []

        for num in nums:
            heapq.heappush(k_th, num)

        for i in range(k - 1):
            heapq.heappop(k_th)

        return -heapq.heappop(k_th)

        
        