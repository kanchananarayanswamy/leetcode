class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while n>0:
            b=n%10
            l.append(b)
            n//=10
        l.sort()
        a=l[-1:-3:-1]
        ans=1
        for i in a:
            ans*=i
        return ans