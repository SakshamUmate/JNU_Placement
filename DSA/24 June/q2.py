def deleteNode(head, x):
    # Code here
    if x==1:
        head=head.next
        return head
    
    i=1
    curr=head
    while curr:
        if (i+1)==x:
            if curr.next.next==None:
                curr.next=None
            else:
                curr.next=curr.next.next
        
        i+=1
        curr=curr.next
        
    return head