class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def fun(n,i,s):
            if len(s[:])==k:
                res.append(s[:])
            for j in range(i,n+1):
                s.append(j)
                fun(n,j+1,s)
                s.pop()
            return res
        return fun(n,1,[])