def DeleteNode(pListHead, pTobeDeleted):
    if not pListHead or not pTobeDeleted:
        return
    #要删除的不是尾节点
    if pTobeDeleted.next != None:
        pNext = pTobeDeleted.next
        pTobeDeleted.val = pNext.val
        pTobeDeleted.next = pNext.next
    #链表只有一个节点，删除头结点（也是尾节点）
    elif pListHead == pTobeDeleted:
        pTobeDeleted = None
        pListHead = None
    #链表中有多个节点，删除尾节点
    else:
        pNode = pListHead
        while pNode.next != pTobeDeleted:
            pNode = pNode.next
        pNode.next = None
        pTobeDeleted = None
