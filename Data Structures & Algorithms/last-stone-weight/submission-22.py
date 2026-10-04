import numpy as np
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        reversestones=[0]*len(stones)
        for i in range(len(reversestones)):
            reversestones[i]=-stones[i]

        
        
        self.maxheap=reversestones
        heapq.heapify(self.maxheap)


        while len(self.maxheap)>2:
            x=heapq.heappop(self.maxheap)
            y=heapq.heappop(self.maxheap)
            if x==y:
                continue
            elif y>x:
                heapq.heappush(self.maxheap,x-y)
                heapq.heapify(self.maxheap)

        if len(self.maxheap)==1:
            return -self.maxheap[0]
        else:
            return self.maxheap[1]-self.maxheap[0]
        
                


        