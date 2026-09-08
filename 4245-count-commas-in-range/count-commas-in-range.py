class Solution:
    def countCommas(self, n: int) -> int:
        # c=0
        # for i in range(1,n+1):
        #     if i>=1000:
        #         c+=1
        # return c
        if n<=999:
            return 0
        return n-999
