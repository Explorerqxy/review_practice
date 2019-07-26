def VerifySequenceOfBST(sequence, length):
    if sequence == None or length <= 0:
        return False
    root = sequence[length-1]
    i = 0
    for i in range(length-1):
        if sequence[i] > root:
            break
    j = i
    for j in range(i, length-1):
        if sequence[j] < root:
            return False
    left = True
    if i > 0:
        left = VerifySequenceOfBST(sequence, i)
    #判断右子树是不是二叉搜索树
    right = True
    if i < length-1:
        right = VerifySequenceOfBST(sequence[i:], length-i-1)
    return left and right
