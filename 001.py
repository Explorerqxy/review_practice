def duplicate(numbers, length):
    if numbers == None or length <= 0:
        return False
    for i in range(length):
        if numbers[i] < 0 or numbers[i] > length -1:
            return False
    res = []
    for i in range(length):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                res.append(numbers[i])
                return res
            #swap numbers[i] and numbers[numbers[i]]
            numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
    return False

#代码中尽管有一个两重循环，但每个数字最多只要交换两次就可以找到属于它的位置，因此总的时间复杂度是O（n）