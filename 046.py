def FindFirstCommonNode(pHead1, pHead2):
    #得到两个链表的长度
    nLength1 = GetListLength(pHead1)
    nLength2 = GetListLength(pHead2)
    nLengthDif = nLength1 - nLength2

    pListHeadLong = pHead1
    pListHeadShort = pHead2
    if nLength2 > nLength1:
        pListHeadLong = pHead2
        pListHeadShort = pHead1
        nLengthDif = nLength2 - nLength1
    #先在长链表上走几步，再同时载两个链表上遍历
    for i in range(nLengthDif):
        pListHeadLong = pListHeadLong.next
    while pListHeadLong != None and pListHeadShort != None and pListHeadLong != pListHeadShort:
        pListHeadLong = pListHeadLong.next
        pListHeadShort = pListHeadShort.next
    #得到第一个公共节点
    pFirstCommonNode = pListHeadLong
    return pFirstCommonNode

def GetListLength(pHead):
    nLength = 0
    pNode = pHead
    while pNode != None:
        nLength += 1
        pNode = pNode.next
    return nLength

