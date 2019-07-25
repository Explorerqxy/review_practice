def MeetingNode(pHead):
    if pHead == None:
        return None
    pSlow = pHead.next
    if pSlow == None:
        return None

    pFast = pSlow.next
    while pFast != None and pSlow != None:
        if pFast == pSlow:
            return pFast
        pSlow = pSlow.next
        pFast = pFast.next
        if pFast != None:
            pFast = pFast.next
    return None

def EntryNodeOfLoop(pHead):
    meetingNode = MeetingNode(pHead)
    if meetingNode == None:
        return None
    #得到环中节点的数目
    nodesInLoop = 1
    pNode1 = meetingNode
    while pNode1.next != meetingNode:
        pNode1 = pNode1.next
        nodesInLoop += 1
    #先移动pNode1，次数为环中节点数目
    pNode1 = pHead
    for i in range(nodesInLoop):
        pNode1 = pNode1.next
    #再移动pNode1和pNode2
    pNode2 = pHead
    while pNode1 != pNode2:
        pNode1 = pNode1.next
        pNode2 = pNode2.next
    return pNode1



