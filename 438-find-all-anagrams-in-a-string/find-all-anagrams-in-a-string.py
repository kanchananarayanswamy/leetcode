class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp={}
        for i in p:
            if i in dp:
                dp[i]+=1
            else:
                dp[i]=1
        i=0
        res=[]
        ds={}
        for j in range(len(s)):
            if s[j] in ds:
                ds[s[j]]+=1
            else:
                ds[s[j]]=1

            if j>=len(p)-1:
                if dp==ds:
                    res.append(i)
                ds[s[i]]-=1
                if ds[s[i]]==0:
                    del ds[s[i]]
                i+=1
        return res
