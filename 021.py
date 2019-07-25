def Merge(pHead1, pHead2):
    if pHead1 == None:
        return pHead2
    if pHead2 == None:
        return pHead1
    pMergedHead = None
    if pHead1.val < pHead2.val:
        pMergedHead = pHead1
        pMergedHead.next = Merge(pHead1.next, pHead2)
    else:
        pMergedHead = pHead2
        pMergedHead.next = Merge(pHead1, pHead2.next)
    return pMergedHead