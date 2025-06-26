# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c=0
        curr= head
        while curr :
            c+=1
            curr= curr.next
        if c%2==1:
            m=math.ceil(c/2)
        else:
            m=(c/2)+1
        
        i=0
        curr = head
        while curr:
            i+=1
            if c%2==1:
                if i==m+1:
                    return curr
                
            else:
                if i==m:
                    return curr
                
            curr=curr.next
        