class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used =[]

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                used.append(nums[i])
                path.append(nums[i])

                backtrack()

                path.pop()
                used.pop()

        backtrack()
        return res