class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d=Counter(s)
        a=d.get(letter,0)
        print(a)
        return a*100//len(s)