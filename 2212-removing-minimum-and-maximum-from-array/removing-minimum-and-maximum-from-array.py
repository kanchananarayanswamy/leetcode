class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        mi=min(nums)
        a=nums.index(mi)
        mx=max(nums)
        b=nums.index(mx)
        
        if(b>a):
            s1=b+1
        else :
            s1=a+1
        print(s1)     

        if(b<a):
            s2=len(nums)-b
        else:
            s2=len(nums)-a
        print(s2)

        if(a<b):
            s33=a+1
        else: 
            s33=b+1

        if(a>b):
            s333=len(nums)-a
        else: 
            s333=len(nums)-b
        s3=s33+s333
        return min(s1,min(s2,s3))
        