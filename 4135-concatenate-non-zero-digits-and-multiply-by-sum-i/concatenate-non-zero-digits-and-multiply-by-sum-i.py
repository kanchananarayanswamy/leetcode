class Solution:
    def count(self,n):
        c=0
        while n>0:
            c+=1
            n//=10
        return c
    def sum(self,n):
        s=0
        while n>0:
            a=n%10
            s+=a
            n//=10
        return s
    def rev(self,n):
        rev=0
        while n>0:
            a=n%10
            rev=rev*10+a
            n//=10
        return rev
    def sumAndMultiply(self, n: int) -> int:
        d=0
        c=self.count(n)
        while n>0:
            a=n%10
            if a!=0:
                d=(d*10)+a
            n//=10
        r=self.rev(d)
        s=self.sum(d)
        return r*s