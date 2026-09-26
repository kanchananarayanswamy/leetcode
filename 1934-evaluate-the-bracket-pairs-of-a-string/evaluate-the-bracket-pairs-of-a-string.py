class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d={}
        for i in knowledge:
            a=i[0]
            b=i[1]
            d[a]=b
        r=""
        i=0
        while i<len(s):
            if s[i]=="(":
                j=i+1
                while s[j]!=')':
                    j+=1
                a=s[i+1:j]
                if a in d:
                    r+=d[a]
                else:
                    r+='?'
                i=j+1
            else:
                r+=s[i]
                i+=1
        return r

                
        


