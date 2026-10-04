class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""

        for i in strs:
            encode+=str(len(i))+"#"+i
        return encode


    def decode(self, s: str) -> List[str]:
        decode=[]
        i=0
        while i<len(s):
            index=s.find("#",i)
            print(s[i:index])
            numberlength = int(s[i:index])
            decode.append( s[index+1:index+1+numberlength] )
            i=index+1+numberlength
        return decode

