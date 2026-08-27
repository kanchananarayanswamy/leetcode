class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i=0
        r=""
        c=0
        l=[]
        for j in range(len(s)):
            if s[j]=="1":
                c+=1
            while c>k:
                if s[i]=="1":
                    c-=1
                i+=1
            if c==k:
                while s[i]=="0":
                    i+=1
                l.append(s[i:j+1])   
        if l:
            mini=min(len(i) for i in l)
            n=[v for v in l if len(v)==mini]
            return min(n)
        return ""