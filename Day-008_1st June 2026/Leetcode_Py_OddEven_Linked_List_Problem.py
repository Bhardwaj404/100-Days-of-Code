# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #to return the reordered list
        curr=head
        node=[]
        while curr:
            node.append(curr.val)
            curr=curr.next
        if len(node)==0:
            return None
        re_node1=[]
        re_node2=[]
        for i in range(0,len(node)):
            if i%2!=0:
                re_node2.append(node[i])
            else:
                re_node1.append(node[i])
        re_node1.extend(re_node2)
        head2=ListNode(re_node1[0])
        curr2=head2
        x=1
        for x in re_node1[1:]:
            curr2.next=ListNode(x)
            curr2=curr2.next
        return head2