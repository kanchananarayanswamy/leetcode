class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def fun(n,i,s):
            if s[:] not in res:
                res.append(s[:])
            for j in range(i,len(n)):
                s.append(n[j])
                fun(n,j+1,s)
                s.pop()
            return res
        return fun(nums,0,[])