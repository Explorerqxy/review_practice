def GetNUmberSameAsIndex(numbers, length):
    if numbers == None or length <= 0:
        return -1
    left = 0
    right = length - 1
    while left <= right:
        middle = left + ((right - left) >> 1)
        if numbers[middle] == middle:
            return middle
        if numbers[middle] > middle:
            right = middle -1
        else:
            left = middle - 1
    return -1

