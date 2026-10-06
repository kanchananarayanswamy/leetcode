class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        c=0
        for i in s:
            if i=="(":
                st.append(i)
            else:
                if st:
                    st.pop()
                else:
                    c+=1
        return len(st)+c