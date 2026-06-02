# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        l=[]
        while curr:
            l.append(curr.val)
            curr=curr.next
        if len(l)==0:
            return None
        k=l.pop(-n)
        if len(l)==0:
            return None
        head2=ListNode(l[0])
        curr2=head2
        for x in l[1:]:
            curr2.next=ListNode(x)
            curr2=curr2.next
        return head2