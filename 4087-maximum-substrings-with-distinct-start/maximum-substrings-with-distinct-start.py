class Solution:
    def maxDistinct(self, s: str) -> int:
        a=set(s)
        return len(a)