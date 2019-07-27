import importlib
m = importlib.import_module('006')

def MoreThanHalfNum(numbers, length):
    if CheckInvalidArray(numbers,length):
        return 0

    middle = length >> 1
    start = 0
    end = length - 1
    index = m.Partition(numbers, length, start, end)
    while index != middle:
        if index > middle:
            end = index - 1
            index = m.Partition(numbers, length, start, end)
        else:
            start = index + 1
            index= m.Partition(numbers,length, start, end)

        result = numbers[middle]
        if not CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result
def CheckInvalidArray(numbers, length):
    g_bInputInvalid = False
    if numbers == None or length <= 0:
        g_bInputInvalid = True
    return g_bInputInvalid

def CheckMoreThanHalf(numbers, length, number):
    times = 0
    for i in range(length):
        if numbers[i] == number:
            times += 1
    isMoreThanHalf = True
    if times*2 <= length:
        g_bInputInvilad = True
        isMoreThanHalf = False
    return isMoreThanHalf


if __name__ == '__main__':
    a = [1,2,2,2,2,2,2,2,5,6,7,8]
    r = MoreThanHalfNum(a, 12)
    print(r)