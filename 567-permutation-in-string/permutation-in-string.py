
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            a=""
            for j in range(i,i+len(s1)):
                a+=s2[j]
            c1=Counter(a)
            if c1==cs:
                return True
        return False