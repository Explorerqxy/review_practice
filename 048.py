def GetMissingNumber(numbers, length):
    if numbers == None or length <= 0:
        return -1
    left = 0
    right = length - 1
    while left <= right:
        middle = (left + right) >> 1
        if numbers[middle] != middle:
            if middle == 0 or numbers[middle - 1] == middle - 1:
                return middle
            right = middle -1
        else:
            left = middle + 1
    if left == length:
        return length
    #无效的输入，比如数组不是按照要求排序的，或者有效数字不在0～n-1范围之内
    return -1
