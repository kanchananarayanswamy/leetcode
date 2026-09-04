class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pre=[0]*n
        maxi=float('-inf')
        post=[0]*n
        mini=float('inf')
        for i in range(n):
            maxi=max(maxi,nums[i])
            pre[i]=maxi
        for i in range(n-1,-1,-1):
            mini=min(mini,nums[i])
            post[i]=mini   
        m=float("-inf")
        for i in range(n):
            a=pre[i]-post[i]
            if a<=k:
                return i
        return -1

