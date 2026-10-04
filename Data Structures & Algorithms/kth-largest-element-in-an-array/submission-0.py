class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap=[-nums[i] for i in range(len(nums))]
        heapq.heapify(maxheap)

        while k!=0:
            element=heapq.heappop(maxheap)
            k=k-1
        return -element

