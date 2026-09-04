class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        r=0
        for i in range(len(nums)):
            a=max(nums[0:i+1])-min(nums[i:len(nums)])
            if a<=k:
                return i
        return -1

