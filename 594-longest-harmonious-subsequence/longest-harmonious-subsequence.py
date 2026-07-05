class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ml=0
        for i in d.keys():
            if i+1 in d:
                ml=max(ml,d[i]+d[i+1])
        return ml