def Print(pRoot):
    if not pRoot:
        return []
    queue = [pRoot]
    outList = []
    while queue:
        res = []
        nextQueue = []
        for point in queue:
            res.append(point.val)
            if point.left != None:
                nextQueue.append(point.left)
            if point.right != None:
                nextQueue.append(point.right)
        outList.append(res)
        queue = nextQueue
    return outList
