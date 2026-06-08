class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def fun(i):
            if i==len(nums):
                res.append(l[:])
                return
            l.append(nums[i])
            fun(i+1) 
            l.pop()
            fun(i+1)     
        res=[]
        l=[]
        fun(0)
        return res