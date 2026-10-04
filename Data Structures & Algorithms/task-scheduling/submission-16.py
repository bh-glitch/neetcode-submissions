import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts=Counter(tasks)
        maxheap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxheap)
        # print(maxheap)

        q=deque()
        time=0
        while maxheap or q:
            time+=1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt<0:
                    q.append([cnt,time+n])
            if q:
                if q[0][1]==time:
                    heapq.heappush(maxheap,q.popleft()[0])
        return time