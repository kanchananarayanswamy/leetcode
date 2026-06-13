class Solution:
    def findMin(self, nums: List[int]) -> int:
        a=nums.index(max(nums))
        if a==len(nums)-1:
            return nums[0]
        return nums[a+1]