class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        d={}
        maxi=float('-inf')
        for i in range(len(s)):
            j=i
            while j<=len(s)-1 and s[j] not in d:
                d[s[j]]=1
                j+=1
            maxi=max(maxi,j-i)
            d={}
        return maxi