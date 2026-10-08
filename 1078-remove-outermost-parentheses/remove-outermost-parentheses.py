class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l=[]
        b=0
        a=0
        for i in range(len(s)):
            if s[i] == '(':
                b+=1
            else:
                b-=1
            if b==0:
                l.append(s[a + 1:i])
                a=i+1
        return ''.join(l)