from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        if len(s)<=3:
            return s
        cnt = Counter(s)

        ans = [""] * len(s)
        i, j = 0, len(s) - 1
        mid = ""

        for ch in sorted(cnt):
            half = cnt[ch] // 2

            while half:
                ans[i] = ch
                ans[j] = ch
                i += 1
                j -= 1
                half -= 1

            if cnt[ch] % 2 == 1:
                mid = ch

        if mid:
            ans[i] = mid

        return "".join(ans)