class Solution:
    def totalFruit(self, f: List[int]) -> int:
        d={}
        m=0
        j=0
        for i in range(len(f)):
            d[f[i]]=d.get(f[i],0)+1
            while len(d)>2:
                d[f[j]]-=1
                if d[f[j]]==0:
                    del d[f[j]]
                j+=1
            m=max(i-j+1,m)
        return m