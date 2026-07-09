class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        re=[]
        rs=""
        cs=Counter(words)
        for i in words:
            rs+=i
        ci=Counter(rs)
        for i in range(len(s)-len(rs)+1):
            c=Counter()
            for j in range(i,i+len(rs),len(words[0])):
                a=s[j:j+len(words[0])]
                c[a]+=1
            if c==cs:
                re.append(i)
            
        return re