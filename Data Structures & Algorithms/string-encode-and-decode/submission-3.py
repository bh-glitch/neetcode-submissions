class Solution:

    def encode(self, strs: List[str]) -> str:
            result=""
            for i in strs:
                result+=str(len(i))+"#"+i

            return result
    # 5#hello5#world
    def decode(self, s: str) -> List[str]:
        result=[]
        ptr=0
        while ptr<len(s):
            index=s.find("#",ptr)
            word_length= int(s[ptr:index])
            result.append(s[index+1:index+1+word_length])
            ptr=index+1+word_length
        return result





        

