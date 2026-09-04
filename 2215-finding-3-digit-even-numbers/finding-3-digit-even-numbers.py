class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        r=[]
        d=Counter(digits)
        for i in range(100,1000,2):
            di=Counter(map(int,str(i)))
            f=1
            for k,v in di.items():
                if v>d[k]:
                    f=0
                    break
            if f:
                r.append(i)
        return r