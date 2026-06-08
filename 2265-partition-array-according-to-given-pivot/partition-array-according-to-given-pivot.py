class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        r=[]
        for i in nums:
            if i<pivot:
                r.append(i)
        for i in nums:
            if i==pivot:
                r.append(i)
        for i in nums:
            if i>pivot:
                r.append(i)
        return r