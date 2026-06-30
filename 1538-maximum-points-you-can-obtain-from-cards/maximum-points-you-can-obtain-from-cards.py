class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        s=0
        for i in range(k):
            s+=cardPoints[i]
        maxi=s
        n=len(cardPoints)
        for j in range(n-1,n-k-1,-1):
            k-=1
            s+=cardPoints[j]-cardPoints[k]
            maxi=max(maxi,s)
        return maxi
