class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c=0
        costs.sort()
        for i in costs:
            coins-=i
            if coins>=0:
                c+=1
        return c


