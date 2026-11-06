class Solution:
    def minMoves(self, nums: List[int]) -> int:
        c=0
        m=max(nums)
        for i in nums:
            if i==m:
                continue
            else:
                c+=(m-i)
        return c 