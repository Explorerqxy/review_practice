def GetFirstK(data, length, k, start, end):
    if start > end:
        return -1
    middleIndex = (start + end) // 2
    middleData = data[middleIndex]
    if middleData == k:
        if (middleIndex > 0 and data[middleIndex -1] != k) or middleIndex == 0:
            return middleIndex
        else:
            end = middleIndex - 1
    elif middleData > k:
        end = middleIndex - 1
    else:
        start = middleIndex + 1
    return GetFirstK(data, length, k, start, end)

def GetLastK(data, length, k, start, end):
    if start > end:
        return -1
    middleIndex = (start + end) // 2
    middleData = data[middleIndex]
    if middleData == k:
        if (middleIndex < length - 1 and data[middleIndex + 1] != k) or middleIndex == length -1:
            return middleIndex
        else:
            start = middleIndex + 1
    elif middleData < k:
        start = middleIndex + 1
    else:
        end = middleIndex - 1
    return GetLastK(data, length, k, start, end)

def GetNumberOfK(data, length, k):
    number= 0
    if data != None and length > 0:
        first = GetFirstK(data, length, k, 0, length - 1)
        last = GetLastK(data, length, k, 0, length - 1)

        if first > -1 and last > -1:
            number = last - first + 1
    return number

if __name__ == '__main__':
    a = [1,2,3,3,3,3,4,5]
    t = GetNumberOfK(a,8,3)
    print(t)
