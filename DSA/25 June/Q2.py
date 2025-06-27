class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s=set()
        curr = head
        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr=curr.next
        
        return False