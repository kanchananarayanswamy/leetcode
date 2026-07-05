class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        need = len(set(nums))
        ans = 0
        n = len(nums)
        for i in range(n):
            st = set()
            for j in range(i, n):
                st.add(nums[j])
                if len(st) == need:
                    ans += 1
        return ans