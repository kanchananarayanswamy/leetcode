class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n=Counter(text)
        c=0
        while (n['b']>=1 and n['a']>=1 and n['l']>=2 and n['o']>=2 and n['n']>=1): 
                c+=1
                n['b']-=1
                n['a']-=1
                n['l']-=2
                n['o']-=2
                n['n']-=1
        return c