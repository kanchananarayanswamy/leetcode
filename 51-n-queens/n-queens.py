class Solution:
    def solveNQueens(self, n):
        res = []
        board = [["."] * n for _ in range(n)]
        def issafe(row,col):
            #check column
            for j in range(n):
                if board[row][j]=="Q":
                    return False
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
        return res












    '''
    def solveNQueens(self, n):
        res = []
        cols, diag1, diag2 = set(), set(), set()
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r-c) in diag1 or (r+c) in diag2:
                    continue
                #place queen
                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                board[r][c] = "Q"

                dfs(r+1)

                #remove queen
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)

        dfs(0)
        return res
    '''