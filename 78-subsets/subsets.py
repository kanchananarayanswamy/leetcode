class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def gen_sub(i,sub_set,res):
            if i==len(nums):
                res.append(sub_set.copy())
                return
            sub_set.append(nums[i])
            gen_sub(i+1,sub_set,res)
            sub_set.pop()
            gen_sub(i+1,sub_set,res)
        gen_sub(0,[],res)
        return res

