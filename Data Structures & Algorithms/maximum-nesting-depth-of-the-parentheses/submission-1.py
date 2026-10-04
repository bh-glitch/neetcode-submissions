class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxcount=0
        for i in s:
            if i == "(":
                count+=1
            if i == ")":
                if maxcount<count:
                    maxcount=count
                count-=1
        return maxcount