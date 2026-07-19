class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            t=n
            s=""
            while t>0:
                a=t%i
                s+=str(a)
                t//=i
            if s != s[::-1]:
                return False
        return True