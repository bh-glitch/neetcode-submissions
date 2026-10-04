class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        #put dictionary in reverse order
        result=[]
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        count=0
        for i in d:
            if(count==k):
                break
            result.append(i)
            count+=1
        return result
            

