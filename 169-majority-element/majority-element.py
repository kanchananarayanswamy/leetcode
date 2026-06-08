class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        n=len(nums)
        for k,v in d.items():
            if v>n//2:
                return k