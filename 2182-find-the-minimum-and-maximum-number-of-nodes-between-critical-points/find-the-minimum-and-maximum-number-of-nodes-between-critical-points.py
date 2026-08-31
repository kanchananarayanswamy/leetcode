# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if (head==None or head.next.next==None):
            return [-1,-1]
        prev=head
        curr=head.next
        c=2
        t=[]
        while curr!=None and curr.next!=None:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                t.append(c)
            prev=curr
            curr=curr.next
            c+=1
        r=[0,0]
        if len(t)<2:
            return [-1,-1]
        mini=float("inf")
        for i in range(len(t)-1):
            mini=min(mini,t[i+1]-t[i])
        r[0]=mini
        r[1]=t[-1]-t[0]
        return r
        




