class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = 0
        sd = {}
        j = 0
        for i in range(len(s)):
            sd[s[i]] = sd.get(s[i], 0) + 1
            while len(sd) == 3:
                c += len(s) - i
                sd[s[j]] -= 1
                if sd[s[j]] == 0:
                    del sd[s[j]]
                j += 1
        return c