def TreeDepth(pRoot):
    if pRoot == None:
        return 0
    nLeft = TreeDepth(pRoot.left)
    nRight = TreeDepth(pRoot.right)
    return nLeft + 1 if (nLeft > nRight) else nRight + 1

def IsBalanced(pRoot, pDepth):
    if pRoot == None:
        pDepth[0] = 0
        return True
    left = [0]
    right = [0]
    if IsBalanced(pRoot.left, left) and IsBalanced(pRoot.right, right):
        diff = left[0] - right[0]
        if diff <= 1 and diff >= -1:
            pDepth[0] = 1 + (left[0] if (left[0] > right[0]) else right[0])
    return False

def isBalanced(pRoot):
    depth = [0]
    return IsBalanced(pRoot, depth)

