# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur=head
        prev=head

        while cur!=None:
            if head.val==val:
                head=head.next
                cur=head
                prev=head
            elif cur.val==val:
                prev.next=cur.next
                cur=cur.next
            else:
                prev=cur
                cur=cur.next
        return head