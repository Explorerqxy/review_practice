def KthNonde(pRoot, k):
    if pRoot == None or k == 0:
        return None
    return KthNodeCore(pRoot, k)

def KthNodeCore(pRoot, k):
    target = None
    if pRoot.left != None:
        target = KthNodeCore(pRoot.left. k)

    if target == None:
        if k == 1:
            target = pRoot
        k -= 1
    if target == None and pRoot.right != None:
        target = KthNodeCore(pRoot.right, k)
    return target

