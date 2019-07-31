def FindNumsAppearOnce(data, length, num):
    if data == None or length <= 2:
        return
    resultExclusiveOR = 0
    for i in range(length):
        resultExclusiveOR ^= data[i]

    indexOf1 = FindFirstBitIs1(resultExclusiveOR)
    num[0] = num[1] = 0
    for j in range(length):
        if IsBit1(data[j], indexOf1):
            num[0] ^= data[j]
        else:
            num[1] ^= data[j]

def FindFirstBitIs1(num):
    indexBit = 0
    while num & 1 == 0:
        num = num >> 1
        indexBit += 1
    return indexBit
def IsBit1(num, indexBit):
    num = num >> indexBit
    return num & 1

if __name__ == '__main__':
    a = [2,4,3,6,3,2,5,5]
    num = [0,0]
    FindNumsAppearOnce(a,8,num)
    print(num)