# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        
        l=[]
        curr=head
        while curr:
            l.append(curr)
            curr=curr.next
        
        temp=l[k-1].val
        r=l[::-1]
        l[k-1].val=r[k-1].val
        r[k-1].val=temp
        return head





