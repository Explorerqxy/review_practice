def Iscontinuous(numbers, length):
    if numbers == None or length < 1:
        return False
    numbers.sort()
    numberOfZero = 0
    numberOfGap = 0
    #统计数组中0的个数
    for i in range(length):
        if numbers[i] == 0:
            numberOfZero += 1
    #统计数组中的间隔数目
    small = numberOfZero
    big = small + 1
    while big < length:
        #两个数相等，有对子， 不可能是顺子
        if numbers[small] == numbers[big]:
            return False
        numberOfGap += numbers[big] - numbers[small] - 1
        small = big
        big += 1
    return False if (numberOfGap > numberOfZero) else True

if __name__ == '__main__':
    a = [1,2,3,0,5]
    t = Iscontinuous(a,5)
    print(t)