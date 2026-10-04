class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:
            encoded+=str(len(i))+"#"+i

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i <len(s):
            index=s.find("#",i)
            numberlength = int(s[i:index])
            
            decoded.append(s[index+1 : index+1+numberlength])
            i=index+1+numberlength
        return decoded
