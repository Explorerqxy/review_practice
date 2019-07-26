def isSymmetrical(pRoot):
    return IsSymmetrical(pRoot,pRoot)

def IsSymmetrical(pRoot1, pRoot2):
    if pRoot1 == None and pRoot2 == None:
        return True
    if pRoot1 == None or pRoot2 == None:
        return False
    if pRoot1.val != pRoot2.val:
        return False
    return IsSymmetrical(pRoot1.left, pRoot2.right) and IsSymmetrical(pRoot1.right, pRoot2.left)
