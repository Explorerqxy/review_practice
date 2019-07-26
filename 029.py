def Print(pRoot):
    if not pRoot:
        return []
    queue = [pRoot]
    outList = []
    flag = 0
    while queue:
        res = []
        nextQueue = []
        for point in queue:
            res.append(point.val)
            if point.left != None:
                nextQueue.append(point.left)
            if point.right != None:
                nextQueue.append(point.right)
        if flag & 0x1:
            outList.append(res)
        else:
            outList.append(res.reverse())
        queue = nextQueue
    return outList