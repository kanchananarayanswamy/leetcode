class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        m=len(fruits)
        n=len(baskets)
        c=0
        for i in range(m):
            for j in range(n):
                if fruits[i]<=baskets[j]:
                    baskets[j]=0
                    c+=1
                    break
        return m-c