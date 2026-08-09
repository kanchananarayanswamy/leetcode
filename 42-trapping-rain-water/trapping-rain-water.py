class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ml=height[0]
        mr=height[r]
        w=0
        while l<r:
            if height[l]<=height[r]:
                l+=1
                ml=max(height[l],ml)
                w+=ml-height[l]
            else:
                r-=1
                mr=max(height[r],mr)
                w+=mr-height[r]
        return w