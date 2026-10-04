import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minheap=[]
        for point in points:
            x=point[0]
            y=point[1]
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(minheap,[distance,point])
            
            

        finalresult=[]
        while k!=0:
            finalresult.append(heapq.heappop(minheap)[1])
            k=k-1
        return finalresult
                
            