class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        l=[]
        crr=head
        while crr:
            l.append(crr)
            crr=crr.next
        i=0
        n=len(l)
        l.reverse()

        for i in range(n - 1):
            l[i].next = l[i + 1]

        l[-1].next = None  
    
        return l[0]