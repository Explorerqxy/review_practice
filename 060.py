def MaxDiff(numbers, length):
    if numbers == 0 or length < 2:
        return 0
    min = numbers[0]
    maxDiff = numbers[1] - min
    for i in range(2, length):
        if numbers[i-1] < min:
            min = numbers[i-1]

        currentDiff = numbers[i] - min
        if currentDiff > maxDiff:
            maxDiff = currentDiff
    return maxDiff

if __name__ == '__main__':
    a = [9,11,8,5,7,12,16,14]
    t = MaxDiff(a, 8)
    print(t)
