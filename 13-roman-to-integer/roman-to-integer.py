class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        r=0
        n=len(s)
        for i,ch in enumerate(s):
            if i+1<n and d[s[i]]<d[s[i+1]]:
                r-=d[ch]
            else:
                r+=d[ch]
        return r
