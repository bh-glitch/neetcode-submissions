class Solution:
# you have ["Hello","World"] becomes 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:
            length = len(i)
            encoded+=str(length)+"#"+i
        
        print(encoded)
        return encoded




    def decode(self, s: str) -> List[str]:
        length=""
        decoded=[]
        i=0
        while i<len(s):
            index=s.find("#",i)
            numberlength = int( s[i:index] )
            print("values of i is", i)
            decoded.append(s[index+1:index+1+numberlength])
            i=index+numberlength+1
        return decoded


            
            
