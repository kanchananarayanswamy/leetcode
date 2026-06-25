class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        maxi=0
        for i in range(len(s)):
            j=i
            while j<len(s) and s[j] not in d :
                d[s[j]]=1
                j+=1
            maxi=max(maxi,j-i)
            d={}
        return maxi