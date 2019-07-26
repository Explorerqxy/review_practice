# calss TreeNode:
# def __init__(self. x)
#     self.val = x
#     self.left = None
#     self.right = None

def PrintFromTopToBottom(pTreeRoot):
    outList = []
    queue = [pTreeRoot]
    while queue != [] and pTreeRoot:
        outList.append(queue[0].val)
        if queue[0].left != None:
            queue.append(queue[0].left)
        if queue[0].right != None:
            queue.append(queue[0].right)
        queue.pop(0)
    return outList