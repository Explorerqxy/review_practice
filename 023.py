def MirrorRecursively(pNode):
    if pNode == None:
        return
    if pNode.left == None and pNode.right == None:
        return
    tmp = pNode.left
    pNode.left = pNode.right
    pNode.right = tmp

    if pNode.left:
        MirrorRecursively(pNode.left)
    if pNode.right:
        MirrorRecursively(pNode.right)
