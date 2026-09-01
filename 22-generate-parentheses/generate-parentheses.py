class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def fun(s,o,c,n,res):
            if (len(s)==n*2):
                res.append(s)
                return 
            if o<n:
                fun(s+"(",o+1,c,n,res)
            if c<o:
                fun(s+")",o,c+1,n,res)
        fun("",0,0,n,res)
        return res
