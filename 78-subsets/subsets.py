class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def gen_sub(i,sub_set,res):
            res.append(sub_set.copy())
            for j in range(i,len(nums)):
                sub_set.append(nums[j])
                gen_sub(j+1,sub_set,res)
                sub_set.pop()
        gen_sub(0,[],res)
        return res