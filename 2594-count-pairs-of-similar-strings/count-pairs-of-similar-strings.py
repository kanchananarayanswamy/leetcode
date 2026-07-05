from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = Counter()
        ans = 0
        for i in words:
            s = "".join(sorted(set(i)))
            print(s)
            ans += d[s]
            d[s] += 1
        return ans