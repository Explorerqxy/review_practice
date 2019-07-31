def FindNumbersWithSum(data, length, sum):
    if length < 1:
        return []
    ahead = 0
    behind = length -1

    while behind > ahead:
        curSum = data[ahead] + data[behind]
        if curSum == sum:
            num1 = data[ahead]
            num2 = data[behind]
            return [num1, num2]
        elif curSum > sum:
            behind -= 1
        else:
            ahead += 1
    return []

if __name__ == '__main__':
    a = [1,2,4,7,11,15]
    t = FindNumbersWithSum(a,6,15)
    print(t)