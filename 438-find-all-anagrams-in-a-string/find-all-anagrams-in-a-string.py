class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount={}
        scount={}
        res = []
        k=len(p)
        for i in p:
            pcount[i] = pcount.get(i, 0)+1
        i=0
        for j in range(len(s)):
            scount[s[j]] = scount.get(s[j], 0)+1
            if j>=k-1:
                if scount==pcount:
                    res.append(i)
                scount[s[i]]-=1
                if scount[s[i]]==0:
                    del scount[s[i]]
                i+=1
        return res