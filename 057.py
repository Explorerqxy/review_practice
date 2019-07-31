def PrintProbability(number):
    if number < 1:
        return
    g_maxValue = 6
    probability1 = [0 for _ in range(g_maxValue * number +1)]
    probability2 = [0 for _ in range(g_maxValue * number +1)]
    probability = [probability1, probability2]
    flag = 0
    for i in range(1, g_maxValue + 1):
        probability[flag][i] = 1
    for k in range(2, number + 1):
        for i in range(k):
            probability[1-flag][i] = 0
        for i in range(k, g_maxValue * k + 1):
            probability[1-flag][i] = 0
            j = 1
            while j <= i and j <= g_maxValue:
                probability[1-flag][i] += probability[flag][i-j]
                j += 1
        flag = 1 - flag
    total = g_maxValue ** number
    for i in range(number, g_maxValue * number + 1):
        ratio = probability[flag][i] / total
        print("{}:{}".format(i, ratio))


if __name__ == '__main__':
    PrintProbability(2)