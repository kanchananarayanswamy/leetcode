class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range(min(nums)+1,max(nums)+1):
            if i not in nums:
                r.append(i)
        return r