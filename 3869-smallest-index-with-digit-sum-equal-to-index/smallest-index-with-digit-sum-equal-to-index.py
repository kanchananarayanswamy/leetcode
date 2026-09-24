class Solution:
    def sum(self,n):
        s=0
        while n>0:
            a=n%10
            s+=a
            n//=10
        return s
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=self.sum(nums[i])
            if a==i:
                return i
        return -1