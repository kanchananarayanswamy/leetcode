class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c=Counter(nums)
        n=len(nums)
        if k==1:
            maxi=-1
            for k,v in c.items():
                if v==1:
                    maxi=max(k,maxi)
            return maxi
        if k==n:
            return max(nums)
        maxi=-1
        a=nums[0]
        b=nums[n-1]
        if c.get(a,0)==1:
            maxi=max(maxi,a)
        if c.get(b,0)==1:
            maxi=max(maxi,b)
        return maxi