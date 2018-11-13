def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1.data < l2.data:
        l3 = l1
        l1 = l1.next
    else:
        l3 = l2
        l2 = l2.next
    temp = l3
    while l1.next is not None and l2.next is not None:
        temp.next = minimum(l1, l2)
        temp = temp.next
        l1 = l1.next if minimum(l1, l2) is l1 else l2 = l2.next
    if l1.next is None:
        temp.next = l2
    else:
        temp.next = l1

        
        


def minimum(l1, l2):
    if l1.data < l2.data:
        return l1
    else:
        return l2
