class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def fun(i):
            res.append(l.copy())
            for j in range(i,len(nums)):
                l.append(nums[j])
                fun(j+1)
                l.pop()
        res=[]
        l=[]
        fun(0)
        return res
        