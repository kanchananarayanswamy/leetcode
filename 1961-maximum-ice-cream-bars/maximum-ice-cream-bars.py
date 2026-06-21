class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c=0
        costs.sort()
        print(costs)
        for i in costs:
            coins-=i
            print(i,coins)
            if coins>=0:
                c+=1
        return c


