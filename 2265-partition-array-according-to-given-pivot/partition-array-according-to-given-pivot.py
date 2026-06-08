class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ls=[]
        le=[]
        ll=[]
        for i in nums:
            if i<pivot:
                ls.append(i)
            elif i==pivot:
                le.append(i)
            elif i>pivot:
                ll.append(i)
        return ls+le+ll
            