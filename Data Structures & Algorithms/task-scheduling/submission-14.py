import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) ##dictionary {char:frequency}
        # print(count)

        maxheap = [ -cnt for cnt in count.values() ]
        time=0
        # print(count)
        heapq.heapify(maxheap)
        # print(maxheap)
        q=deque()
        while maxheap or q:
            # print("the maxheap is",maxheap)
            # print("the queue is ", q)
            time+=1
            if maxheap:
                cnt = 1+heapq.heappop(maxheap)
                if cnt<0:
                    q.append([cnt,time+n])
            
            if q:
                if q[0][1]==time:
                    heapq.heappush(maxheap,q.popleft()[0])
                    
        return time