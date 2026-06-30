class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        mini=float("inf")
        i=0
        for j in range(len(nums)):
            s+=nums[j]
            while  s>=target:
                mini=min(mini,(j-i)+1)
                s-=nums[i]
                i+=1
        if mini==float("inf"):
            mini=0
        return mini