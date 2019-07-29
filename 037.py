g_InvalidInput = False
def FindGreatestSumOfSubArray(pData, nLength):
    if pData == None or nLength <= 0:
        global g_InvalidInput
        g_InvalidInput = True
        return 0
    g_InvalidInput = False

    nCurSum = 0
    nGreatestestSum = -float('inf')
    for i in range(nLength):
        if nCurSum <= 0:
            nCurSum = pData[i]
        else:
            nCurSum += pData[i]
        if nCurSum > nGreatestestSum:
            nGreatestestSum = nCurSum
    return nGreatestestSum

if __name__ == '__main__':
    a =[1,-2,3,4,5,6,-6,-7,7,-9]
    t = FindGreatestSumOfSubArray(a,10)
    print(t)
    m = -float('inf')
    print(m)