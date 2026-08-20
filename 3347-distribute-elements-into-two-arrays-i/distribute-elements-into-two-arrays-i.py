class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[nums[0]]
        b=[nums[1]]
        for i in range(2,n):
            if a[-1]>b[-1]:
                a.append(nums[i])
            else:
                b.append(nums[i])                
        return a+b