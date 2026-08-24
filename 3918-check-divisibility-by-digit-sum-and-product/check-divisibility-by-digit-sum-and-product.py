class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        ds=0
        while temp>0:
            ds+=temp%10
            temp//=10
        temp2=n
        dp=1
        while temp2>0:
            dp*=temp2%10
            temp2//=10
        a=ds+dp
        if n%a==0:
            return True
        return False