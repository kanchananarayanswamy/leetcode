class Solution:
    def isValid(self, s: str) -> bool:
        ss=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                ss.append(i)
            else:
                if (ss and (( ss[-1]=="(" and i==")") or (ss[-1]=="[" and i=="]") or (ss[-1]=="{" and i=="}"))):
                    ss.pop()
                else:
                    return False
        if ss:
            return False
        return True
