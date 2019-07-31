def FindContinuousSequence(sum):
    if sum < 3:
        return
    small = 1
    big = 2
    middle = (1 + sum) // 2
    curSum = small + big

    while small < middle:
        if curSum == sum:
            PrintContinuousSequence(small, big)
        while curSum > sum and small < middle:
            curSum -= small
            small += 1
            if curSum == sum:
                PrintContinuousSequence(small, big)
        big += 1
        curSum += big

def PrintContinuousSequence(small, big):
    s = []
    for i in range(small, big + 1):
        s.append(i)
    print(s)

if __name__ == '__main__':
    FindContinuousSequence(9)

