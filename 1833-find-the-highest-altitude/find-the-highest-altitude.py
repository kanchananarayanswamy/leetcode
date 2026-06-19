class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=[0]
        m=0
        for i in gain:
            m+=i
            maxi.append(m)
        return max(maxi)