def HasSubtree(pRoot1, pRoot2):
    result = False
    if pRoot1 != None and pRoot2 != None:
        if Equal(pRoot1.dbval, pRoot2.dbval):
            result = DoesTree1HaveTree2(pRoot1,pRoot2)
        if not result:
            result = HasSubtree(pRoot1.pLeft, pRoot2)
        if not result:
            result = HasSubtree(pRoot1.pRight, pRoot2)
    return result

def DoesTree1HaveTree2(pRoot1,pRoot2):
    if pRoot2 == None:
        return True
    if pRoot1 == None:
        return False
    if not Equal(pRoot1.dbval, pRoot2.dbval):
        return False
    return DoesTree1HaveTree2(pRoot1.pLeft, pRoot2.pLeft) and DoesTree1HaveTree2(pRoot1.pRight, pRoot2.pRight)

def Equal(num1, num2):
    if num1 - num2 > -0.0000001 and num1 - num2 < 0.0000001:
        return True
    else:
        return False

