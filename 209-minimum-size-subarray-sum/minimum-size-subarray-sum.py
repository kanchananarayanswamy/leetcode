class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        m=float("inf")
        s=0
        for j in range(len(nums)):
            s+=nums[j]
            while s>=target:
                m=min(m,j-i+1)
                s-=nums[i]
                i+=1
        if m==float("inf"):
            m=0
        return m