class Solution:
    def getRow(self, rowIndex : int) -> List[int]:
        res=[]
        for i in range(rowIndex+1):
            l=[1]*(i+1)
            res.append(l)
        for r in range(2,rowIndex+1):
            for c in range(1,len(res[r])-1):
                res[r][c]=res[r-1][c-1]+res[r-1][c]
        return res[rowIndex]
            