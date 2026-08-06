class Solution:
    def digit_pro(self,n):
        a=1
        while n>0:
            s=n%10
            a*=s
            n//=10
        return a
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,100+1):
            if self.digit_pro(i)%t==0:
                return i