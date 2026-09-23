class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        t=sum(nums)-x
        if t<0:
            return -1
        j=0
        s=0
        m=-1
        for i in range(len(nums)):
            s+=nums[i]
            while s>t:
                s-=nums[j]
                j+=1
            if s==t:
                m=max(m,(i-j)+1)
        if m==-1:
            return -1
        return len(nums)-m
            
        