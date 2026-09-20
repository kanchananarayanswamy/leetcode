class Solution:
    def reverseDegree(self, s: str) -> int:
        c=0
        p=1
        for i in s:
            a=(26+(97-ord(i)))
            c+=a*p
            p+=1
        return c