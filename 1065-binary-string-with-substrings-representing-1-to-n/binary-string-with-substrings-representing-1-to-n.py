class Solution:
    def queryString(self, s: str, n: int) -> bool:
        r=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                f=s[i:j+1]
                a=int(f,2)
                r.append(a)
        for i in range(1,n+1):
            if i not in r:
                return False
        return True
        