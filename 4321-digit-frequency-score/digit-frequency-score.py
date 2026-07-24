class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        for i in str(n):
            d[i]=d.get(i,0)+1
        s=0
        for i,j in d.items():
            a=int(i)*j
            s+=a
        return s