class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        s=str(n)
        r=""
        for i in s:
            if i!="0":
                r+=i
        n1=int(r)
        su=0
        for i in r:
            su+=int(i)
        return n1*su

