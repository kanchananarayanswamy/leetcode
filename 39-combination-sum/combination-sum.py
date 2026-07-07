class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        temp=[]
        def fun(i,temp,res):
            if sum(temp)==target:
                res.append(temp.copy())
                return
            if sum(temp)>target or i>=len(candidates):
                return
            temp.append(candidates[i])
            fun(i,temp,res)
            temp.pop()

            fun(i+1,temp,res)
        fun(0,temp,res)
        return res
