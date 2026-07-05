class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = [["."] * n for _ in range(n)]
        def issafe(row,col):
            #check column
            # for j in range(n):
            #     if board[row][j]=="Q":
            #         return False
            for i in range(n):
                if board[i][col]=="Q":
                    return False
            #check left diagonal
            i,j=row-1,col-1
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            #check right diagonal
            i,j=row-1,col+1
            while i>=0 and j<n:
                if board[i][j]=="Q":
                    return False
                i-=1
                j+=1
            return True
        def fun(row):
            if row==n:
                res.append(["".join(i) for i in board])
                return
            for col in range(n):
                if issafe(row,col):
                    board[row][col]="Q"
                    fun(row+1)
                    board[row][col]="."
        fun(0)
        return len(res)