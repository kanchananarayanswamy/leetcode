class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        while len(nums)>1:
            n=len(nums)
            l=[0]*(n//2)
            for i in range(n//2):
                if i%2==0:
                    l[i]=min(nums[2 * i], nums[2 * i + 1])
                else:
                    l[i]=max(nums[2 * i], nums[2 * i + 1])
            nums=l
        return l[0]