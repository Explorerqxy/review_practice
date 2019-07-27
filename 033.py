def Permutation(pStr):
    if pStr == None:
        return
    permutation(pStr, pStr)

def permutation(pStr, pBegin):
    if pBegin == len(pStr):
        print(pStr)
    else:
        for pCh in range(pBegin, len(pStr)):
            temp = pStr[pCh]
            pStr[pCh] = pStr[pBegin]
            pBegin = temp

            permutation(pStr, pBegin + 1)

            pStr[pBegin], pStr[pCh] = pStr[pCh], pStr[pBegin]
