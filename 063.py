def GetNodePath(pRoot, pNode, path):
    if pRoot == pNode:
        return True
    path.append(pRoot)

    found = False
    i = pRoot.chilren.begin
    while not found and pRoot.children.end:
        found = GetNodePath(i, pNode, path)
    if not found:
        path.pop()
    return found

def GetLastCommonNode(path1, path2):
    iterator1 = 0
    iterator2 = 0
    pLast = None
    while iterator1 != len(path1) and iterator2 != len(path2):
        if path1[iterator1] == path2[iterator2]:
            pLast = path1[iterator1]
        else:
            break
        iterator1 += 1
        iterator2 += 1
    return pLast

def GetLastCommonParent(pRoot, pNode1, pNode2):
    if pRoot == None or pNode1 == None or pNode2 == None:
        return None
    path1 = []
    GetNodePath(pRoot, pNode1, path1)
    path2 = []
    GetNodePath(pRoot, pNode2, path2)
    return GetLastCommonNode(path1, path2)

