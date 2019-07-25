def FindKthTOTail(pListHead, k):
    if pListHead == None or k == 0:
        return None
    pAhead = pListHead
    pBehind = None

    for i in range(k):
        if pAhead.next != None:
            pAhead = pAhead.next
        else:
            return None

    pBehind = pListHead
    while pAhead.next != None:
        pAhead = pAhead.next
        pBehind = pBehind.next
    return pBehind

