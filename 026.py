def IsPopOrder(pPush, pPop, nLength):
    bPossible = False
    if pPush != None and pPop != None and nLength > 0:
        pNextPush = pPush
        pNextPop = pPop
        stackData = []
        while pNextPop < nLength:
            while stackData.empty() or stackData.top() != pPop[pNextPop]:
                if pNextPush == nLength:
                    break
                stackData.push(pPush[pNextPush])
                pNextPush += 1
            if stackData.top() != pPop[pNextPop]:
                break
            stackData.pop()
            pNextPop += 1
        if stackData.empty() and pNextPop == nLength:
            bPossible = True
    return bPossible
