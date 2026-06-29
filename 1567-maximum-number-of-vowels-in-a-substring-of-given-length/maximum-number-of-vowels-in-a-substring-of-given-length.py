class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c=0
        v='aeiou'
        for i in range(k):
            if s[i] in v:
                c+=1
        m=c
        for i in range(k,len(s)):
            if s[i] in v:
                c+=1
            if s[i-k] in v:
                c-=1
            m=max(c,m)
        return m
