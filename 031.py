def FindPath(pRoot, exceptedSum):
    if pRoot == None:
        return
    path = []
    currentSum = 0
    findPath(pRoot, exceptedSum, path, currentSum)

def findPath(pRoot, exceptedSum, path, currentSum):
    currentSum += pRoot.val
    path.append(pRoot.val)
    #如果是叶节点，并且路径上节点值的和等于输入的值，则打印出这条路径
    isLeaf = pRoot.left == None and pRoot.right == None
    if currentSum ==exceptedSum and isLeaf:
        print(path)
    #如果不是叶节点，则遍历它的子节点
    if pRoot.left != None:
        findPath(pRoot.left, exceptedSum, path, currentSum)
    if pRoot.right != None:
        findPath(pRoot.right, exceptedSum, path, currentSum)
    #在返回父节点之前，在路径上删除当前节点
    path.pop()
