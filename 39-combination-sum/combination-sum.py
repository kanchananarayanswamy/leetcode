class Solution:
    def combinationSum(self, n: List[int], k: int) -> List[List[int]]:
        res = []
        a = []

        def fun(i):
            if sum(a) == k:
                res.append(a[:])
                return

            if i >= len(n) or sum(a) > k:
                return

            a.append(n[i])
            fun(i)      # reuse same element
            a.pop()

            fun(i + 1)  # move to next element

        fun(0)
        return res