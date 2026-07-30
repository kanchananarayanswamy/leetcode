class Solution:
    def minimumPushes(self, word: str) -> int:
        c=0
        for i in range(len(word)):
            c+=(i//8)+1
        return c