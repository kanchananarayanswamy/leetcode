class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        p=0
        l=0
        for i in d.values():
            p+=i//2
            l+=i%2
        return [p,l]