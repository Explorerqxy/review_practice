class ComplexListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.sibling = None

def CloneNodes(pHead):
    pNode = pHead
    while pNode != None:
        pCloned = ComplexListNode()
        pCloned.val = pNode.val
        pCloned.next = pNode.next
        pCloned.sibling = pNode.sibling

        pNode.next = pCloned
        pNode = pCloned.next

def ConnectSiblingNodes(pHead):
    pNode = pHead
    while pNode != None:
        pCloned = pNode.next
        if pNode.sibling != None:
            pCloned.sibling = pNode.sibling.next
        pNode = pCloned.next

def ReconnectedNodes(pHead):
    pNode = pHead
    pClonedHead = None
    pClonedNode = None

    if pNode != None:
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedNode.next
        pNode = pNode.next

    while pNode != None:
        pClonedNode.next = pNode.next
        pClonedNode = pClonedNode.next
        pNode.next = pClonedNode.next
        pNode = pNode.next
    return pClonedHead

def Clone(pHead):
    CloneNodes(pHead)
    ConnectSiblingNodes(pHead)
    return ReconnectedNodes(pHead)



