def InversePairs(data, length):
    if data == None or length < 0:
        return 0
    copy = [0 for _ in range(length)]
    for i in range(length):
        copy[i] = data[i]
    count = InversePairCore(data, copy, 0, length-1)
    return count

def InversePairCore(data, copy, start, end):
    if start == end:
        copy[start] = data[start]
        return 0
    length = (end - start) // 2
    left = InversePairCore(copy, data, start, start + length)
    right = InversePairCore(copy, data, start + length + 1, end)
    #i初始化为前半段最后一个数字的下标
    i = start + length
    #j初始化为后半段最后一个数字的下标
    j = end
    indexCopy = end
    count = 0
    while i >= start and j >= start + length + 1:
        if data[i] > data[j]:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
            count += j - start - length
        else:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
    for m in range(i, start-1, -1):
        copy[indexCopy] = data[m]
        indexCopy -= 1
    for n in range(j, start + length, -1):
        copy[indexCopy] = data[n]
        indexCopy -= 1

    return left + right + count

if __name__ == '__main__':
    a = [7,5,6,4]
    t = InversePairs(a, 4)
    print(t)
    print(a)
