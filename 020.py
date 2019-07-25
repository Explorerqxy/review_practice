def ReverseList(pHead):
    pReversedHead = None
    pNode = pHead
    pPrev = None
    while pNode != None:
        pNext = pNode.next
        if pNext == None:
            pReversedHead = pNode
        pNode.next = pPrev
        pPrev = pNode
        pNode = pNext
    return pReversedHead