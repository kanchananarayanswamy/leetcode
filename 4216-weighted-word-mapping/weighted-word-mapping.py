class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        l=[]
        for i in words:
            sumi=0
            for j in range(len(i)):
                a=ord(i[j])-97
                sumi+=weights[a]
            l.append(chr(122-sumi%26))
        return "".join(l)
