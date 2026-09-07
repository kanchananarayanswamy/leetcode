class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=[0]*(len(s)+1)
        dp[0]=1
        d={}
        for i in range(1,len(s)+1):
            c=s[i-1]
            dp[i]=2*dp[i-1]
            if c in d:
                dp[i]-=dp[d[c]-1]   # d[c] is previously seen index
            d[c]=i
        return (dp[len(s)]-1)%(MOD)