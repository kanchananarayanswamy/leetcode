class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        r = []
        while k > 0:
            key = max(d, key=d.get)
            r.append(key)
            del d[key]
            k -= 1
        return r