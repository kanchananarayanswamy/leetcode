class Solution:
    def maxDistinct(self, s: str) -> int:
        a=Counter(s)
        return len(a)