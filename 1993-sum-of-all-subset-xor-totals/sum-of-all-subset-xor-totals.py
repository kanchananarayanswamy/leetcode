class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=[]
        def fun(i,sub,ans):
            ans.append(sub.copy())
            for j in range(i,len(nums)):
                sub.append(nums[j])
                fun(j+1,sub,ans)
                sub.pop()
        fun(0,[],ans)
        s=0
        for i in ans:
            a=0
            for j in i:
                a^=j
            s+=a
        return s
